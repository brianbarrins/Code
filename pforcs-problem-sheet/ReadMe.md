# All files contained in this will be standardised by the following comments

# Author: Brian Barrins
# Student ID: G00299967
# Email: G00299967@GMIT.IE

______________________
# WEEK2 BMI
# Purpose:
This program allows any user to input their height and weight and then displays their BMI and gives them an indication as to what this means

# Comments:
The user input is stored in two separate variables, which are then computed against eachother to calculate the BMI
I added a separate if elseif statement to create classifications for a BMI in the ranges
The classification is done by comparing the output versus predefined values

# Week 3 BitCoin Price
# Purpose:
This program allows any user to determine the current price for Bitcoin in the three major Western world currencies
______________________
# Comments:
When looking at the json file and the printout in the terminal, it was very hard to see what the structure was visually
I opened the data in Notepad++ and formatted it better there and saw the structure of the file with the different indentations

Using the bpi as the highest level, I can now pick each of the sub categories and their attributes individually
Using the rawest form of the float data: rate_float as the output avoids any potential issues with the comma in the normal rate. This would be for potential future proofing/parsing of data
______________________
# Week 4 -Number calculator
# Purpose:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

# Comments:
Relatively straight forward while loop acting as the control and exit criteria
If and elif statements controlling conditional actions for the internal calculations
______________________
# Week 5 - custom square root
# Purpose:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)
I suggest that you look at the newton method at estimating square roots
______________________
# Comments:
Stepped example of the use of Newton's estimation of a squared root applied to a function

Initially started the fucntion with the aim of using another For and If loop to iterate and guess the numbers. This turned out to be much less straight forward than had planned.
______________________
# Week 6 - read file and output search data
# Purpose:
Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line.

# Comments:
First attempt was made using very basic and straight forward code

Second attempt had the function built in as well as giving the user to search for any character that they wanted
______________________
# Week 7 - Regex
# Purpose:
Write a program called extract-url.py, that will extract the URLs from an access.log file.
ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)
The program should store the URLs as strings in a list.

# Comments:
First part initially tried different ways. Settled on a look forward/look back regex for text between the "T " in GET and POST and the end of the url ending in " HTTP"
This differentiates from any other random Ts or http in the file.
Output to list and print list ok.

Struggling to find a logical way to output to dictionary....cannot find a split method good enough
Trying to use a regex expression to split the list out again before dictionary. Not sure if this will work though.
______________________
# Week 8 - Matplot lib
# Purpose:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
Some marks will be given for making the plot look nice.

# Comments:
straight forward attempt using the standard english method of using matplot through structured call outs showing readability

Secondary attempt to illustrate additional options for markers and a logrythmic scale (which didn't really look nice IMO)
______________________
# Week 9 - data download access.log
# Purpose:
I want to find which sessionId downloaded the most data
Read the access.log into a dataframe (see lab)
Set the date time to be the index (you will need to manipulate this data, see lab)
Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
Use groupBy to get the sum of all the data downloaded by each sessionId.
Create a plot of this (type of your choice)

# Comments:
Initial load and basic data frame creation and cleansing.
Removal of unneeded columns and square brackets
Regex to remove and solate the session Id
Grouped the data by Session ID to concatenate the data used values.

Created a plot of the data to show data usage overtime keeping the initial index sequence so as to keep the data temporal.

Hardest one yet for sure
______________________
# Week 10 - bomb proof list average
# Purpose:
Write a (bullet proof) function called averageTo(aList, toIndex)
The function should take in a list and an index. 
The function will return the average of the numbers upto and including the toIndex in the aList.
When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)
Write the code to test all the things that could go wrong with this function, and a test to check the function does work.
The test code can be in the same file or different file.

# Comments:
Decided to go about it from two ways
Option 1: Main method for development and testing to save constant user input
Setup the second function for the actual calculation and the for loops
Introduced errors and checks in the calculation function to check soundness

Option 2: Figured a better approach would be to stop the data being entered in the first place
Created optional user input method
Checked each individual input and threw errors and continue for all possible and encountered scenarios in developmen
______________________