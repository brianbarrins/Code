#Weekly Tasks
#7. Write a program called extract-url.py, that will extract the URLs from an access.log file.
#ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)
#The program should store the URLs as strings in a list.

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

import re

filename = "./files/access.log"
urllist = []

with open (filename,"r") as f:
	count = 0
	for line in f:
	#using a look forward and look back command for regex
		expr = "(?<=T )(.*)(?=HTTP )"
		url = re.findall(expr, line)
		#print(url)
		urllist.append(url)
		count += 1
		
print ("The instances of urls in this file are: {}".format(count))
print(urllist)


#Extra (This is extra work for few marks so think about if it is worth doing)

#Store the URLs as a Dictionary object in the list with the resource and parameter names and values separated out
for i in urllist:

	spliteres = r'(?<=\&).+?(?=\=)'
	splitparam = r'(?<=\=).+?(?=\&)'
	
	res = re.findall(spliteres,line)
	param = re.findall(splitparam,line)
#	print (res)
#	print (param)