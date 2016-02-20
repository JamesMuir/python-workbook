#SUM UP 10 RANDOMS [2]
from random import randint

repeating = True
while repeating:
    total = 0
    numbers = []
    for i in range(10):
        numbers.append(randint(1,1000))
        total += numbers[i]

    print(numbers)
    print("The total of the above numbers are {}.".format(total))
    
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
