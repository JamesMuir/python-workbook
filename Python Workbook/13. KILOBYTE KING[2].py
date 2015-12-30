#KILOBYTE KING[2]
from commonFunctions import *

repeating = True 
while repeating:
    gettingData = True
    while gettingData:
        numberOfKilobytes = int_input("Enter the numbers of kilobytes: ")
        while True:
            print("The number of kilobytes is {}.".format(numberOfKilobytes))
            informationCheck = input("Is the above information correct? Enter Y/N: ").lower()
            if informationCheck == "y":
                gettingData = False
                break
            elif informationCheck == "n":
                break
            else:
                print("Enter Y/N.")

    numberOfBytes = numberOfKilobytes * 1024
    numberOfBits = numberOfBytes * 8

    print("The number of bytes is {} and the number of bits is {}.".format(numberOfBytes, numberOfBits))
    
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
