#Weekly Tasks
#1. Write a program that calculates somebody's Body Mass Index (BMI).
# The inputs are the person's height in centimetres and weight in kilograms.
# The output  is their weight divided by their height in metres squared.

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

#create variables for height and weight and BMI
#use of float to allow for decimals and computations
height = float(input("Please enter your height in Centimetres: "))
#convert to metres for calculation
hm = height*0.01
weight = float(input("Please enter your weight in Kilograms: "))
#formula = weight * height squared (using**2 in lieu of height * height)
bmi = weight/(hm**2)

#classifications
    #underweight: <18
    #healthy: 18-25
    #overweight: 25-29
    #obese: 30-39
    #extremelyobese: 40+
#source: https://www.hse.ie/eng/services/list/2/primarycare/east-coast-diabetes-service/management-of-type-2-diabetes/lifestyle-management/healthy-eating-advice/bmi-chart.pdf

#simple if and else if statements based on mathematical float value for bmi
#reference for example: https://www.programiz.com/python-programming/if-elif-else
if bmi < 18:
    classification = "Underweight"
elif bmi < 25:
     classification = "Healthy"   
elif bmi < 29:
     classification = "Overweight"  
elif bmi < 39:
     classification = "Obese"  
elif bmi >40:
     classification = "Extremely Obese"  

print ("Your Body Mass Index (BMI) is: {} \nThis makes you: {}".format(bmi,classification) )