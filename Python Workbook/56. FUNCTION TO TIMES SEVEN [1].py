#FUNCTION TO TIMES SEVEN [1]
from commonFunctions import int_input

def timesSeven(number):
    return number * 7

repeating = True
while repeating:
    userNumber = int_input("Please enter a decimal number: ")
    print(timesSeven(userNumber))

    print()
    while True:
        print("Do you want to repeat.")
        userWantToReapeat = input("Enter Y/N: ").lower()
        if userWantToReapeat == "y":
            break
        elif userWantToReapeat == "n":
            repeating = False
            break
    
