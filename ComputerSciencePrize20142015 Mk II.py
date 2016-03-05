# ComputerSciencePrize20142015 Mk II 
from random import randint
from turtle import Screen, Turtle

#Works out the distance betweem two points 
def getDistance(pointOne, pointTwo):
    lengthOne = pointOne[0] - pointTwo[0]
    lengthTwo = pointOne[1] - pointTwo[1]

    lengthOneSquared = lengthOne * lengthOne
    lengthTwoSquared = lengthTwo * lengthTwo

    lengthThreeSquared = lengthOneSquared + lengthTwoSquared

    lengthThree = lengthThreeSquared ** 0.5

    return lengthThree

def getRouteDistance(routeName, startingPoint, pointA, pointB, pointC, endingPoint):
    global routes
    
    route = 0
    route += getDistance(startingPoint, pointA)
    route += getDistance(pointA, pointB)
    route += getDistance(pointB, pointC)
    route += getDistance(pointC, endingPoint)
    routes += [[routeName, route, startingPoint, pointA, pointB, pointC, endingPoint]]

#Creates an empty array to store points  
points = []

#Generates five random points and adds them to 
for i in range(5):
    randomOne = randint(-24,25)
    randomTwo = randint(-24,25)

    points += [[randomOne,randomTwo]]

#Picks a random starting point and removes it from the points array
startingPoint = points[randint(0,4)]
points.remove(startingPoint)

#Picks a random ending point and removes it from the points array
endingPoint = points[randint(0,3)]
points.remove(endingPoint)

routes = []
    
getRouteDistance("Route One", startingPoint, points[0], points[1], points[2], endingPoint)
getRouteDistance("Route Two", startingPoint, points[1], points[2], points[0], endingPoint)
getRouteDistance("Route Three", startingPoint, points[2], points[0], points[1], endingPoint)
getRouteDistance("Route Four", startingPoint, points[0], points[2], points[1], endingPoint)
getRouteDistance("Route Five", startingPoint, points[1], points[0], points[2], endingPoint)
getRouteDistance("Route Six", startingPoint, points[2], points[1], points[0], endingPoint)

routesSorted = sorted(routes,key=lambda l:l[1])

print(routesSorted[0])

#Turtle graphics 
scale = 15
window = Screen()
cursor = Turtle()
cursor.penup()
cursor.goto(routesSorted[0][2][0] * scale, routesSorted[0][2][1] * scale)
cursor.pendown()
for i in range(3):
    cursor.goto(routesSorted[0][i+3][0] * scale, routesSorted[0][i+3][1] * scale)
cursor.goto(routesSorted[0][6][0] * scale,routesSorted[0][6][1] * scale)

window.mainloop()    



