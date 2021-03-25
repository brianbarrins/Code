#Weekly Task 10:
#Write a (bullet proof) function called averageTo(aList, toIndex)
#The function should take in a list and an index. 
#The function will return the average of the numbers upto and including the toIndex in the aList.
#When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)
#Write the code to test all the things that could go wrong with this function, and a test to check the function does work.
#The test code can be in the same file or different file.



#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#Optional code1
#pre-populated list option
#aList = [1,5,65,43,13,14,19,-2,2.7,'a']
#user generated list option

aList=[]

#Optional code 2
def checkmanualinput(message):
    n = int(input("Enter how many numbers you would like to use: "))
    while True:
        try:
            for i in range(0,n):
                userInput = int(input(message))
                #get the positive of the number to avoid negative numbers
                aList.append(abs(userInput))       
        except ValueError:
            #will catch floats and strings and any non integers
            print("Not a positive integer! Try again from the start, using only numbers.")
            aList=[]
            continue
        else:
            return userInput 
            break 
     
num = checkmanualinput("Enter a set of numbers to calculate the average: ")
#I do not personally see a need for the index as each item is already indexed by its placeholder.
#however creating an index for the end limit regardless
toIndex = len(aList)-1

print("The list: ",aList, " will be used to calculate the average of the list.")
newlist = []

#use cases
'''
Check for the following:
text - check to string
check for decimal and round
minus  check for minus and make positive
'''
def averageTo(list,index):
    i=0
    #Code written here as a double check that the list is correct
    #Code is included for the possible use case above of a previously populated list where erroneous entries occur in the list
    #second optional approach for solution
    try:
        for x in aList:
            if isinstance(x,float):
                print("\nThe non-integer value: '{}' in position: {} is being rounded upwards in the list and will be included as a positive integer\n".format(x,i))
                #other option using raise exception
                #raise ValueError("No Non-integer values are allowed!!!\n\nThe non-integer value: '{}' in position: {} is being rounded upwards in the list and will be included as a positive integer).format(x,i))
                '''x = round(x)
                x=int(x)
                x=abs(x)
                newlist.append(x)'''

                
            elif x<=0:
                print("\nThe negative value: '{}' in position: {} is being altered in the list and will be included as a positive integer\n".format(x,i))
                #other option using raise exception
                #raise ValueError("Negative numbers are not allowed!!!\n\nThe negative value: '{}' in position: {} is being altered in the list and will be included as a positive integer\n").format(x,i))
                '''x=x*-1
                newlist.append(x)'''
            #make positive
            x=abs(x)
            #round it (to deal with floats)
            x=round(x)
            #output to newlist
            newlist.append(x)
            #increase counter for indexing position
            i=i+1
#code here for type error:
    except TypeError:
            print("\nThe string value: '{}' in position: {} is being removed from the list and will not be included in the calculation\n".format(x,i))
            aList.remove(x)
#code here for zero division error:            
    except ZeroDivisionError:
        print("You must enter some numbers first!!\n\nBack to the start and let's try again.")
        checkmanualinput("Enter a set of numbers to calculate the average: ")
    #finally:
    #create average and ensure it's initialised
    workingavg = 0
    #get average
    workingavg = sum(newlist)/len(newlist)
    print("The Average of the list: {} is: {}".format(newlist,workingavg))

averageTo(aList,toIndex)
