#TECH CRITIC[3]
from commonFunctions import *

repeating = True
xbox = -5
playstation = -5
PC = -5

while repeating:
    gettingData = True
    while gettingData:
        print()
        while ((xbox > 0) and (xbox < 11)) != True:
            xbox = int_input("Please enter a rating for the Xbox One out of ten: ")
        while ((playstation > 0) and (playstation < 11)) != True:
            playstation = int_input("Please enter a rating for the PS4 out of ten: ")
        while ((PC > 0) and (PC < 11)) != True:
            PC = int_input("Please enter a rating for the PC out of ten: ")

        print("You entered the following:")
        print("You rated the Xbox One as {} out of Ten.".format(xbox))
        print("You rated the Playstation as {} out of Ten.".format(playstation))
        print("You rated the PC as {} out of Ten.".format(PC))

        print()
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

    print()
    if PC > xbox and PC > playstation:
        print("Well done the PC is better that the PS4 and Xbox One.")
    if xbox > playstation:
        print("Correct the Xbox One is better than the PS4.")
    if playstation > xbox:
        print("Incorrect the PS4 is not better than the Xbox One.")
    if playstation > PC:
        print("The PS4 is not better than the PC.")
    
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
