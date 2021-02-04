#randomnum.py

import random

lower = int(input("Please enter the lower limit: "))
upper = int(input("Please enter the upper limit: "))

number = random.randint(lower,upper)
print ("here is a random number: {} between {} and {}".format(number,lower,upper))