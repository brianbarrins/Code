#Weekly Tasks
#4. Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#get users input as an integer
number = int(input("Please input a positive integer: "))
#sets final exit parameter
while number !=1:
    #establishes if number is even
    if number%2==0:
        #divide by 2
        number=number//2
    #using elif statement for odd (could also use else)    
    elif number%2==1:
        #multiply by 3 and add 1
        number=(number*3)+1 
    #print the numberand loop
    print (number)

#print ("0")    