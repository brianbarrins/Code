#lab2.py
#This program takes user entered information and displays a greeting
#this will also send an email to the specified host
#author:brianbarrins

#create variables for name and age storage
name = input("Please enter your name: ")
host = input("Please enter your host: ")
#create print statement using dynamically referenced objects
print("Hello {} \t, Nice to meet you!\nYour host: {} will be here to see you shortly".format(name, host))