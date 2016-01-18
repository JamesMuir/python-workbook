#THREE NUMBER SORT[2]
from commonFunctions import *

repeating = True
while repeating:
    numbers = [0,0,0]
    for i in range(3):
        numbers[i] = int_input("Please enter number {}: ".format(i))

    numbers.sort()

    for i in range(3):
        print(numbers[i])
        
    while True:
        userRepeat = input("\nDo you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            print()
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")

            
