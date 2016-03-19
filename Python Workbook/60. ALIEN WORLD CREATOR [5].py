#ALIEN WORLD CREATOR [5]
from random import randint 
from commonFunctions import int_input

def alienWorldCreator():
    radiusKm = randint(3000, 100000) 
    massKg = radiusKm * randint(1, 5) * (10 ** 24) 
    if randint(0,1) == 1:
        isInhabited = True
    else:
        isInhabited = False
    color = [hex(randint(0,255)),hex(randint(0,255)),hex(randint(0,255))]
    
    return [radiusKm, massKg, isInhabited, color]

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        numberOfPlanets = int_input("Enter the number of planets in the solar system: ")

        print()
        print("Is the above correct?")
        while True:
            dataCorrect = input("Enter Y/N: ")
            if dataCorrect == "y":
                gettingData = False
                break
            elif dataCorrect == "n":
                break

    solarSystem = []
    for i in range(numberOfPlanets):
        solarSystem.append(alienWorldCreator())

            
    for i in solarSystem:
        print(i)

    print()
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        
