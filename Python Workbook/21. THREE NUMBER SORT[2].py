#THREE NUMBER SORT[2]
from commonFunctions import *

repeating = True
while repeating:
    numbers = []
    for i in range(3):
        numbers.append(int_input("Please enter number {}: ".format(i+1)))

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

            
