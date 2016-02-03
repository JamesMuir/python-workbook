#LUCKY NUMBER TOTAL[2]
from commonFunctions import *
from random import randint

repeating = True
totalNumbers = 3
while repeating:
    gettingData = True
    while gettingData:
        numbers = []
        for i in range(totalNumbers):
            while True:
                number = int_input("Please enter the number {} (between one and five): ".format(i+1))
                if number >= 1 and number <= 5: 
                    numbers.append(number)
                    break
                else:
                    print("Between one and five.")

        print("Your three numbers are: {}.".format(numbers))
        while True:
            isInformationCorrect = input("Is the above information correct. Enter Y/N: ").lower()
            if isInformationCorrect == "y":
                gettingData = False
                break
            elif isInformationCorrect == "n":
                break
            else:
                print("Enter Y/N.")
                print()

    #Gets the total of the users number
    total = 0
    for i in numbers:
        total += i

    randomNumber = 0
    for i in range(totalNumbers):
        randomNumber += randint(1,5)

    if randomNumber == total:
        print("You guessed the lucky number.")
    elif randomNumber != total:
        print("You did not guess the lucky number your number was {} and the lucky number was {}.".format(total, randomNumber))
        
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
