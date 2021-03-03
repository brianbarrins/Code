#Weekly Tasks
#6. Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#new
filename ="./files/" + input ("Please type the name of the file you would like to use: ")

#simpler way without added complexity
with open (filename,'rt') as f:
	#parse data to data variable
	data = f.read()
	counters = data.count("e") + data.count("E")
	print ("The number of e's/E's in the file {} is: ".format(filename),counters)

#added for user input
searchfor = input ("Please type what additional character you would like to search for: ")
#function to search custom character and conversion to upper and lower
def customsearch():
	with open (filename, 'rt') as f:
		data = f.read()
		#added option for custom search
		countsearch = data.count(searchfor.upper()) + data.count(searchfor.lower())
		print ("The number of {}'s in the file {} is: ".format(searchfor,filename),countsearch)

customsearch()
