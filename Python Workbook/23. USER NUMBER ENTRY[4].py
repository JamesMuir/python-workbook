#USER NUMBER ENTRY[4]
from commonFunctions import *

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        while True:
            numberOne = float_input("Please enter a number between one and twenty: ")
            if numberOne >= 1 and numberOne <= 20:
                break
            else:
                print()
                
        while True:
            numberTwo = float_input("Please enter a number between one and fifty: ")
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
        while True:
            operation = input("Do you want to add or multiply? \nEnter A or M: ").lower()
            if operation == "a" or operation == "m":
                break
            else:
                print("Enter A or M.\n")

        if operation == "a":
            print("You choose to add.")
        elif operation == "m":
            print("You choose to multiply.")

        while True:
            print()
            pickingOperationData = input("Is the above information correct. Enter Y/N: ").lower()
            if pickingOperationData == "y":
                pickingOperation = False
                break
            elif pickingOperationData == "n":
                break
            else:
                print("Enter Y/N.")
                print()

    if operation == "a":
        output = numberOne + numberTwo
        print("You two number added together are {}.".format(output))
    elif operation == "m":
        output = numberOne * numberTwo
        print("You two number multiplied together are {}.".format(output))

    print()
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")



    
