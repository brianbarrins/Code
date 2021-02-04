import math
points = [(1,1),(2,2),(3,3),(4,2),(5,1)]

for x, y in points:
    dist = math.sqrt(x**2 + y**2)
    print ("Point({},{} is {:.3f} , from the origin".format(x,y,dist))