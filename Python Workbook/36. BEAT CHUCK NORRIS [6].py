#BEAT CHUCK NORRIS [6]
from random import randint
from commonFunctions import int_input

repeating = True
while repeating:
    chuckNorris = 10
    player = 10
    while True:
        numbers = [randint(1,1000),randint(1,1000)]
        secretNumber = randint(0,1)
            
        print("The two numbers are {} and {}.".format(numbers[0],numbers[1]))
        
        chuckGuess = randint(0,1)
        while True:
            userGuess = int_input("Please select the first or second number. Enter 1 or 2: ") - 1
            if userGuess == 0 or userGuess == 1:
                break

        if secretNumber == userGuess:
            player += 1
        else:
            player -= 1
            
        if secretNumber == chuckGuess:
            chuckNorris += 1
        else:
            chuckNorris -= 1
        
        print("Chuck Norris has {} points and you have {} points.".format(chuckNorris, player))

        if player == 20:
            print("The player wins")
            break
        if chuckNorris == 20:
            print("Chuck Norris wins")
            break

        if player == 0:
            print("Chuck Norris wins")
            break
        if chuckNorris == 0:
            print("The player wins")
            break 

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
