#WORD GUESSING GAME[3 or 4]
from random import randint

words = ["spam", "potato", "soul", "cake", "pi", "banana", "strawberry", "random", "integer", "float"]

repeating = True
while repeating:
    #Picks a random word
    randomWord = words[randint(0, len(words)-1)]

    gettingData = True
    while gettingData: 
        print("You have a option of easy, normal or hard mode.")
        difficulty = input("Enter E/N/H: ").lower()
        if difficulty == "e":
            turns = 6
            gettingData = False
        elif difficulty == "n":
            turns = 5
            gettingData = False
        elif difficulty == "h":
            turns = 4
            gettingData = False

    print("You have {} turns.".format(turns))
        
    for i in range(turns):
        guess = input("Please enter a word: ")
        if guess == randomWord:
            print("Well done you've guessed the word.")
            break
        elif guess != randomWord:
            print("Incorrect.")
            randomNumber = randint(0, len(randomWord)-1)
            randomLetter = randomWord[randomNumber]
            if randomNumber == 0:
                print("The first letter in the word is {}.".format(randomLetter))
            elif randomNumber == 1:
                print("The second letter in the word is {}.".format(randomLetter))
            elif randomNumber > 1:
                print("The {}th letter in the word is {}.".format(randomNumber + 1, randomLetter))
            
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

                
