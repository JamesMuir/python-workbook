#DICE ROLL COUNTER [2]
from random import randint

repeating = True
while repeating:
    #Total amounts (1,2,3,4,5,6)
    totals = [0,0,0,0,0,0]
    
    for i in range(100):
        x = randint(0,5)
        if x == 0:
            totals[0] += 1
        elif x == 1:
            totals[1] += 1
        elif x == 2:
            totals[2] += 1
        elif x == 3:
            totals[3] += 1
        elif x == 4:
            totals[4] += 1
        elif x == 5:
            totals[5] += 1  

    for i in range(6):
        print("The total for {} is {}.".format(i+1, totals[i]))

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
