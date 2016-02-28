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

    for i in range(5):
                
