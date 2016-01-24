# ComputerSciencePrize20142015
import random

#Works out the distance betweem two points 
def getDistance(pointOne, pointTwo):
    lengthOne = pointOne[0] - pointTwo[0]
    lengthTwo = pointOne[1] - pointTwo[1]

    lengthOneSquared = lengthOne * lengthOne
    lengthTwoSquared = lengthTwo * lengthTwo

    lengthThreeSquared = lengthOneSquared + lengthTwoSquared

    lengthThree = lengthThreeSquared ** 0.5

    return lengthThree
    
#Creates a 50 by 50 grid
grid = [[0 for x in range(50)] for y in range(50)]

#Creates an empty array to store points  
points = []

#Generates five random points and adds them to 
for i in range(5):
    randomOne = random.randint(0,49)
    randomTwo = random.randint(0,49)

    grid[randomOne][randomTwo] = 1
    points += [[randomOne,randomTwo]]

#Picks a random starting point
startingPoint = points[random.randint(0,4)]
points.remove(startingPoint)

#Picks a random ending point
endingPoint = points[random.randint(0,3)]
points.remove(endingPoint)

routeOne = 0
routeOne += getDistance(startingPoint, points[0])
routeOne += getDistance(points[0], points[1])
routeOne += getDistance(points[1], points[2])
routeOne += getDistance(points[2], endingPoint)

print(routeOne)

routeTwo = 0
routeTwo += getDistance(startingPoint, points[1])
routeTwo += getDistance(points[1], points[2])
routeTwo += getDistance(points[2], points[0])
routeTwo += getDistance(points[0], endingPoint)

print(routeTwo)

routeThree = 0
routeThree += getDistance(startingPoint, points[2])
routeThree += getDistance(points[2], points[0])
routeThree += getDistance(points[0], points[1])
routeThree += getDistance(points[1], endingPoint)

print(routeThree)

routeFour = 0
routeFour += getDistance(startingPoint, points[0])
routeFour += getDistance(points[0], points[2])
routeFour += getDistance(points[2], points[1])
routeFour += getDistance(points[1], endingPoint)

print(routeFour)

routeFive = 0
routeFive += getDistance(startingPoint, points[1])
routeFive += getDistance(points[1], points[0])
routeFive += getDistance(points[0], points[1])
routeFive += getDistance(points[1], endingPoint)

print(routeFive)

routeSix = 0
routeSix += getDistance(startingPoint, points[2])
routeSix += getDistance(points[2], points[1])
routeSix += getDistance(points[1], points[0])
routeSix += getDistance(points[0], endingPoint)

print(routeSix)
