#VIKING NAME GENERATOR [3]
from random import randint

listOne = ["alf", "udu", "enkson", "ebba"]
listTwo = ["ikin","gron","hine","kon"]

repeating = True
while repeating:
    print("{}{}".format(listOne[randint(0,3)],listTwo[randint(0,3)]))
    
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

