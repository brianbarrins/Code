#div.py
first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))

answer= first // second
remainder = first%second
print("The answer of {} divided by {} is: {} with remainder {}".format(first, second, answer, remainder))
