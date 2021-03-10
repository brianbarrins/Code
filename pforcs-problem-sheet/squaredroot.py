#Weekly Tasks
#5. Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x)
#I suggest that you look at the newton method at estimating square roots

#Author: Brian Barrins
#Student ID: G00299967
#Email: G00299967@GMIT.IE


#using formula root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.  from: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/


def squaredroot (number,n=500):
	value = float(number)
	for i in range(n):
		#squareroot being taken as a positive number (and secondary function later for minus number)
		number = 0.5 * (number + value / number)
		neganswer = -1*(number)
	return "The Squared root of {} is approximately: {} and {} ".format(value,number,neganswer)

test = squaredroot(float(input("Please input a positive number to calculate it's Squared root: ")))
print(test)


#Extra coding attempt for my own entertainment and my initial attempt until I saw the Newton's method in the hint!!!

#attempt at solution with for and if loop	
#using numpy code from: https://stackoverflow.com/questions/51024356/how-can-i-use-floating-point-number-for-increment-in-for-loop-by-python

def othersqrt (number):
	#get users input as a float
	number = float(number)
	#round up number as upper limit for iterations. Sqrt cannot be higher than number itself
	roundedinput = round(number)
	import numpy
	for i in numpy.arange(0,roundedinput,0.1):
		result=i*i
		actual=round(result)	
		if number > actual:
			i=i
			#print(i,"increasing",actual)
		elif number < actual:
			i=i-1.15
			# print(i,"decreasing",actual)
		elif number == actual:
			#working backwards by finding two numbers (one number)multiplied by itself that would equal the value
			x=float(i)
			break
	return ("The Squared root of {} is approximately {} and {}".format (number,x,x*-1))


othertest = othersqrt(float(input("Please input a positive number to calculate it's Squared root: ")))
print(othertest)