import random

queue = []
limit = int(input("Please select the number of queue items: "))
for n in range(0,limit):
    rand = random.randint(1,100)
    queue.append(rand)

print("The queue is currently: {}".format(queue))

while len(queue) !=0:
    #pop removes first item
    currentnumber = queue.pop(0)
    print("Current number is: {} and the queue is: {}".format(currentnumber,queue))

print ("The queue is now empty")    