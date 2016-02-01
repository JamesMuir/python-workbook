#MOVIE MOMENTS [1]
from random import randint
randomQuotes = ["{}, you can not know the power of the dark side of the force.",
                "{}, you are the droid I am looking for.",
                "{}, you were only supose to blow the bloody doors off.",
                "{}, get to the chopper."
               ]

repeating = True
while repeating:
    gettingData =True
    while gettingData:
        name = input("What is your name? ")

        print("Your name is {}.".format(name))
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

    print(randomQuotes[randint(0, len(randomQuotes)-1)].format(name))
     
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
