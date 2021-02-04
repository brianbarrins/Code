inputstring=input("Please enter a string: ")
outputlist = inputstring.split(" ")

for output in outputlist:
    print (output)

#positioning
#from end
#[-1]
#from start
#[1]
#from 1 to end
#[1:]
#from start to 5
#[:5]
#in reverse
#[::-1]

lastfive = inputstring[-5:]
lastfiveeverysecond = inputstring[-5::2]
print(lastfive)
print(lastfiveeverysecond)