#EVERRANDOM [3-5]
from random import randint
from commonFunctions import int_input

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        lowestValue = int_input("Please enter the lowest value: ")
        highestValue = int_input("Please enter the highest value: ")

        print("You selected a random number between {} and {}.".format(lowestValue, highestValue))
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

    randomNumber = randint(lowestValue, highestValue)
    if randomNumber == 7:
        print("Well done you go the lucky number - 7.")
    else:
        print(randomNumber)
            
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
