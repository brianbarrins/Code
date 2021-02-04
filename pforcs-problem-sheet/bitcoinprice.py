#Weekly Tasks
#1.Write a program(bitcoin.py)that outputs the current bitcoin price in US Dollars.
# #You may use the code snippet below to get a Dict object that contains the price.
#2.Extra output all the price in the threecurrencies,in a neatway

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

import requests

url="https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()
print(bitCoinDict)

#when looking at the json file and the prinout in the terminal, it was very hard to see what the structure was
#I opened the data in Notepad++ and saw the structure of the file with the different indentations

#using the bpi as the highest level, I can now pick each of the sub categories and their attributes individually
#using the rawest form of the float data: rate_float
usdprice=bitCoinDict["bpi"]["USD"]["rate_float"]
gbpprice=bitCoinDict["bpi"]["GBP"]["rate_float"]
eurprice=bitCoinDict["bpi"]["EUR"]["rate_float"]

print ("The price of Bitcoin is: \n\tUSD: ${}\n\tGBP: £{}\n\tEUR: €{}".format(usdprice,gbpprice,eurprice))