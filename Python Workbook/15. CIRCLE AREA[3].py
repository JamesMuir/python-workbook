#CIRCLE AREA[3] circumference
from commonFunctions import *
import math

repeating = True 
while repeating:
    gettingData = True
    while gettingData:
        print()
        radiusOrDiameterKnown = input("Do you know the radius or the diameter? Enter Y/N: ").lower()
        if radiusOrDiameterKnown == "y":
            while True:
                radiusOrDiameter = input("Is it the radius or diameter you know? Enter R/D: ").lower()
                if radiusOrDiameter == "r":
                    radius = float_input("Please enter the radius: ")
                    break
                elif radiusOrDiameter == "d":
                    diameter = float_input("Please enter a diameter: ")
                    break
                else:
                    print("Please enter R or D.")
                    print()

            while True:
                if radiusOrDiameter == "r":
                    print("The radius is {}.".format(radius))
                elif radiusOrDiameter == "d":
                    print("The diameter is {}.".format(diameter))
                        
                informationCheck = input("Is the above information correct. Enter Y/N: ")
                if informationCheck == "y":
                    gettingData = False
                    break 
                elif informationCheck == "n":
                    break
                                   
        elif radiusOrDiameterKnown == "n":
            while True:
                circumferenceKnown = input("Do you know the circumference? Enter Y/N: ").lower()
                if circumferenceKnown == "y":
                    circumference = float_input("Please enter the circumference: ")
                    break
                elif circumferenceKnown == "n":
                    print("If you don't know the radius, diameter or circumference you can't work out the area.")
                    gettingData == False
                    break
                else:
                    print("Please enter y or n.")
    
            while True:
                if circumferenceKnown == "y":
                    print("The circumference is {}.".format(circumference))
                    informationCheck = input("Is the above information correct. Enter Y/N: ")
                    if informationCheck == "y":
                        gettingData = False
                        break 
                    elif informationCheck == "n":
                        break

                elif circumferenceKnown == "n":
                    gettingData = False
                    break
                
        else:
            print("Please enter y or n.")
            break

    if radiusOrDiameterKnown == "y":
        if radiusOrDiameter == "r":
            area = radius ** 2 * math.pi 
            print("The area is {}.".format(area))
        elif radiusOrDiameter == "d":
            radius = diameter/2
            area = radius ** 2 * math.pi 
            print("The area is {}.".format(area))
    elif radiusOrDiameterKnown == "n":
        if circumferenceKnown == "y":
            radius = circumference/math.pi/2
            area = radius ** 2 * math.pi 
            print("The area is {}.".format(area))
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
