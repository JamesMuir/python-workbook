#USER NUMBER ENTRY[4]
from commonFunctions import *

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        while True:
            numberOne = int_input("Please enter a number between one and twenty: ")
            if numberOne >= 1 and numberOne <= 20:
                break
            else:
                print()
                
        while True:
            numberTwo = int_input("Please enter a number between one and fifty: ")
            if numberTwo >= 1 and numberTwo <= 50:
                break
            else:
                print()

        print("Your two numbers are {} and {}.".format(numberOne, numberTwo))        
        while True:
            isInformationCorrect = input("Is the above information correct. Enter Y/N: ").lower()
            if isInformationCorrect == "y":
                gettingData = False
                break
            elif isInformationCorrect == "n":
                break
            else:
                print("Enter Y/N.")
                print()

    pickingOperation = True
    while pickingOperation:
        operation = input("Do you want to add or multiply? \nEnter A or W: ").lower()
        if operation == "a" or operation == "w":
            break
        else:
            print("Enter A or W.\n")

    
