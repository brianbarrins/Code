#Weekly task 9:
#I want to find which sessionId downloaded the most data
#    Read the access.log into a dataframe (see lab)
#    Set the date time to be the index (you will need to manipulate this data, see lab)
#    Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
#    Use groupBy to get the sum of all the data downloaded by each sessionId.
#    Create a plot of this (type of your choice)

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#import functions
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

#set file name and location
#filename = "./Files/access.log"
#sample file for better readibility
filename = "./Files/sample.txt"

#read file to df
#create column names for parsing
colnames= ["IP","Dash1","Dash2","Time", "URL","Response","Packet Size","User Agent", "Unknown","Unknown1"]
sample = pd.read_csv(filename, sep=" ",header=None)
#assign column names
sample.columns=colnames
#view df
#print(sample)
#upon viewing I will drop these columns as they are not useful
sample = sample.drop(columns=['Response','User Agent','Dash1','Dash2','Unknown','Unknown1'])

#code from tutorials
#simple strip of brackets
sample["Time"] = sample["Time"].str.strip('[]')
#format date & time
sample["Time"] = pd.to_datetime(sample["Time"], format='%d/%b/%Y:%H:%M:%S')

#set date time to be index manipulate
sample=sample.set_index(["Time"])
#view and check data
print("Initial File: \n",sample)

#use regex to extract session id to new column apply
#using apply method from labs
def GetSessionID(url):
    #using a look forward and look back command for regex
	#https://www.rexegg.com/regex-lookarounds.html
    expr = "(?<=JSESSIONID=).* (?=HTTP)"
    newvalue = re.search(expr,url).group()
    return newvalue

#create SessionID column now for new just session ID
sample['Session ID'] = sample['URL'].apply(GetSessionID)
#test view
print ("Sample with new Session ID Column: \n",sample)

#group by sum of data per session
#make new df for ease of backing out
#df=sample[['Session ID','Packet Size']].copy()
#print(df)
#group data by session ID and sum total the packet size
df=sample.groupby(['Session ID']).sum('Packet Size')
df.rename(columns={"Packet Size":"Total Data per Session"},inplace=True)
print(df)
#reset index so session Id can be used
df=df.reset_index()
#print(df)

#assign values for graphs
x=df['Session ID']
y=df['Total Data per Session']
#create plot
#plot line scatter
plt.plot(x,y)
plt.xlabel("Session ID")
plt.ylabel("Size of data per session")
plt.title("Total Data per Session ID")
plt.show()
#plot bar chart
plt.bar(x,y,color="blue")
plt.xlabel("Session ID")
plt.ylabel("Size of data per session")
plt.title("Total Data per Session ID")
plt.show()

#neither graph yields much visual information for the file size

#Extra:
#I have not written this code myself so I don't know how hard it is......
#Work out the amount of data each sessionId downloaded in any given day

#newdf = sample['2021/02/15 23:00':'2021/02/15 23:59:59']
sample['Day'] = sample.index
sample['Day'] = sample['Day'].astype(str)
sample['Day']=sample['Day'].str.split(":",expand=True)
dfextra=sample.groupby(['Day','Session ID']).sum('Packet Size')
dfextra.rename(columns={"Packet Size":"Total Data per Session per day"},inplace=True)
print(dfextra)