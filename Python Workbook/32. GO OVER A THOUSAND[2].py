#GO OVER A THOUSAND [2]
from commonFunctions import int_input

repeating = True
while repeating:
    total = 0
    while total < 1000:
        total += int_input("Please enter a number: ")
        print("The total so far is {}.".format(total))
        if total > 1000:
            print("Well done on going over a thousand.")
        
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
            
