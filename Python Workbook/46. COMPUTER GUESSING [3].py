#COMPUTER GUESSING [3]
from commonFunctions import int_input
from random import randint 

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        userNumber = int_input("Please enter a number between 1 and 100: ")
        if userNumber >= 1 and userNumber <= 100:
            print("You entered {}.".format(userNumber))
            isInputCorrect = input("Please enter Y/N: ").lower()
            if isInputCorrect == "y":
                gettingData = False
            elif isInputCorrect == "n":
                print()
                    
        else:
            print("In what world is {} between 1 and 100?".format(userNumber))

    lowValue = 1
    maxValue = 100
    for i in range(50):
        guess = randint(lowValue, maxValue)
        while True:
            print("Is your guess higher or lower than {} or is it correct.".format(guess))
            isHigherOrLower = input("Enter H/L/C: ").lower()
            if isHigherOrLower == "h":
                lowValue = guess
                break
            elif isHigherOrLower == "l":
                maxValue = guess
                break
            elif isHigherOrLower == "c":
                print("The computer correctly guess")
