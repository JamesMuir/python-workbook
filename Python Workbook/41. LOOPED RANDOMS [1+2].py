#LOOPED RANDOMS [1]
from random import randint
from commonFunctions import int_input

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        lowestValue = int_input("Please enter the lowest value: ")
        highestValue = int_input("Please enter the highest value: ")

        print("You selected a random number between {} and {}.".format(lowestValue, highestValue))
        print("Is this correct?")
        while True: 
            dataRight = input("Enter Y/N: ").lower()
            if dataRight == "y":
                gettingData = False
                break
            elif dataRight == "n":
                break
        
        
    for i in range(100):
        print(randint(lowestValue,highestValue))
        
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
