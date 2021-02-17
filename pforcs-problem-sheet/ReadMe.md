# All files contained in this will be standardised by the following comments
# Author: Brian Barrins
# Student ID: G00299967
# Email: G00299967@GMIT.IE

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

# Comments:
When looking at the json file and the printout in the terminal, it was very hard to see what the structure was visually
I opened the data in Notepad++ and formatted it better there and saw the structure of the file with the different indentations

Using the bpi as the highest level, I can now pick each of the sub categories and their attributes individually
Using the rawest form of the float data: rate_float as the output avoids any potential issues with the comma in the normal rate. This would be for potential future proofing/parsing of data

# Week 4 -Number calculator
# Purpose:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

# Comments:
Relatively straight forward while loop acting as the control and exit criteria
If and elif statements controlling conditional actions for the internal calculations

# Week 5 - custom square root
# Purpose:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)
I suggest that you look at the newton method at estimating square roots

# Comments:
Stepped example of the use of Newton's estimation of a squared root applied to a function

Initially started the fucntion with the aim of using another For and If loop to iterate and guess the numbers. This turned out to be much less straight forward than had planned.