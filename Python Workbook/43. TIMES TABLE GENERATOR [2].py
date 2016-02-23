#TIMES TABLE GENERATOR [2]
from commonFunctions import float_input
from random import randint

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        timesTable = float_input("Please enter the times table you want: ")

        print("You selected the {} times table.".format(timesTable))
        while True:
            inputRight = input("Enter Y/N: ").lower()
            if inputRight == "y":
                gettingData = False
                break
            elif inputRight == "n":
                break
        
    for i in range(20):
        total = (i+1) * timesTable
        print("{} * {} = {}".format(i+1, timesTable, total))

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
