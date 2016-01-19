#BIGGER OR SMALLER[3]
from commonFunctions import *

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        numberOne = float_input("Enter number one: ")
        numberTwo = float_input("Enter number two: ")

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
                
    if numberOne > numberTwo:
        difference = numberOne - numberTwo
        print("Number one is bigger than number two, the difference is {}.".format(difference))
        
    elif numberOne < numberTwo:
        difference = numberTwo - numberTwo
        print("Number two is bigger than number one, the difference is {}.".format(difference))

    elif numberOne == numberTwo:
        print("The two numbers are the same.")
        
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
