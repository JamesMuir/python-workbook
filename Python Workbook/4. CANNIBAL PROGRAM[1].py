#CANNIBAL PROGRAM[1]
import random

repeating = True
responses = ["Hello, {} people with {} hair and {} eyes are very tasty in the cooking pot!",
            "Hello, {} people with {} hair and {} eyes are very tasty over the fire!",
            "Hello, {} people with {} hair and {} eyes smell horrible when set on fire!"
            ]

while repeating:
    userName = input("Please enter your name: ")
    hairColour = input("Please enter your hair colour: ")
    eyeColour = input("Please enter your eye colour: ")

    randomResponseNumber = random.randint(0, len(responses)-1)
    
    print(responses[randomResponseNumber].format(userName, hairColour, eyeColour))

    while True: 
        userReapeat = input("Do you want to repeat? Enter Y/N: ").lower()
        if userReapeat == "y":
            break
        elif userReapeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
