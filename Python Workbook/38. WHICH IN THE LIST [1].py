#WHICH IN THE LIST [1]
from commonFunctions import int_input

strings = ["Alpha", "Gamma", "Beta"]

repeating = True
while repeating:
    
    while True:
        itemNumber = int_input("Please select a number between ") - 1
        if itemNumber >= 0 and itemNumber <= 2:
            break

    print(strings[itemNumber])
    
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
