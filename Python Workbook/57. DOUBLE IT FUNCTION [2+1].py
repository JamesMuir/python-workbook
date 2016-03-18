#DOUBLE IT FUNCTION [2+1]
from commonFunctions import int_input

def doubleIt(number):
    return number * 2

repeating = True
while repeating:
    userNumber = int_input("Please enter a decimal number: ")
    print(doubleIt(userNumber))    

    print()
    while True:
        print("Do you want to repeat?")
        repeat = input("Enter Y/N: ").lower()
        if repeat == "y":
            break
        elif repeat == "n":
            repeating = False
            break
