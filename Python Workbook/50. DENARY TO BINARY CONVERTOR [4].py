#DENARY TO BINARY CONVERTOR [4]
from commonFunctions import int_input

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        denaryNumber = int_input("Please enter a number between 0-255: ")
        if denaryNumber >= 0 and denaryNumber <= 255:
            while True:
                print("You entered {}.".format(denaryNumber))
                isDataCorrect = input("Is this correct? Enter Y/N: ").lower()
                
                if isDataCorrect == "y":
                    gettingData = False
                    break
                elif isDataCorrect == "n":
                    break
    
    
    
    binaryNumber = bin(denaryNumber)

    print("{} in binary is {}.".format(denaryNumber, binaryNumber[2:]))

    
    print()
    while True:
        print("Do you want to repeat?")
        repeat = input("Enter Y/N: ").lower()
        if repeat == "y":
            break
        elif repeat == "n":
            repeating = False
            break
