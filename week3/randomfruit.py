#randomfruit.py

import random
#list
fruit = ["Apple", "Orange", "Bannana", "Pear", "Pineapple"]
#tuple (cannot be changed once made)
#fruit = ("Apple", "Orange", "Bannana", "Pear", "Pineapple")


#we want a random number between 0 and len-1
index=random.randint(0,len(fruit)-1)
#select object in that position
randfruit = fruit[index]
print("A random fruit is: {}".format(randfruit))