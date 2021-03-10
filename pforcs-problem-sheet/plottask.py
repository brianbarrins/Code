#Weekly Tasks
#8. Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

#Some marks will be given for making the plot look nice.

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE

import numpy as np
import matplotlib.pyplot as plt
import pandas as pa


x=4
#increase array by 1 for starting position
xplot = np.array(range(1,x+1))
yplot = xplot
#squared
y2plot = xplot*xplot
#cubed
y3plot = xplot*xplot*xplot
#plot individual points as a coloured lines
plt.plot(xplot, yplot, label = "f(x)=x",color = "blue",marker = "o", ms = "5",ls="-")
plt.plot(xplot, y2plot, label = "g(x)=x2", color = "red",marker= "s", ms = "7.5",ls="--")
plt.plot(xplot, y3plot, label = "h(x)=x3", color = "green",marker= "^", ms = "10",ls=":")
plt.legend()
plt.title("Plot of the value of x={} as a function of f(x)=x, g(x)=x2 and h(x)=x3".format(x))
plt.show()

#alternative more user friendly to look at way
#additional options provided by markers from: https://www.w3schools.com/python/matplotlib_markers.asp

#providing option for user to input should they wish
x = int(input("Please enter a value for X: "))
print ("\n\nThis will now be used to calculate and display \n f(x)=x \n g(x)=x2 \n h(x)=x3 ")
xplot = np.array(range(1,x+1))
yplot = xplot
#squared
y2plot = xplot*xplot
#cubed
y3plot = xplot*xplot*xplot
#plot in one line
plt.plot(xplot, xplot, 'bs', xplot, xplot**2, 'rh', xplot, xplot**3, 'g^')
#optional log scale (which doesn't look great)
plt.yscale('log')
plt.show()