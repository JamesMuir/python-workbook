#RANDOMISER TOTAL [1]
from random import randint

repeating = True
while repeating:
    randomNumbers = []
    for i in range(3):
        randomNumbers.append(randint(1,1000))
        print(randomNumbers[i])

    total = 0
    for i in range(3):
        total += randomNumbers[i]

    print("The total is: {}".format(total))

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
