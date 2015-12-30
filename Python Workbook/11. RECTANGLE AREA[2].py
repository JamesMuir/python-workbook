#RECTANGLE AREA[2]
from commonFunctions import *

repeating = True 
while repeating:
    gettingData = True
    while gettingData:
        print()
        width = float_input("Please enter the width (cm): ")
        length = float_input("Please enter the length (cm): ")
        print()
        while True:
            print("The width is {} cm and the length is {} cm.".format(width, length))
            informationCheck = input("Is the above information correct? Enter Y/N: ".format(width, length)).lower()
            if informationCheck == "y":
                gettingData = False
                break
            elif informationCheck == "n":
                break
            else:
                print("Enter Y/N.")

    area = width*length
    print("The area is {} cm.".format(area))

    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")


