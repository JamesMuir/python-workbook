#FORTUNE COOKIE [1]
from random import randint

fortunes = ["A friend asks only for your time not your money.",
            "Today it's up to you to create the peacefulness you long for.",
            "Enjoy the good luck a companion brings you.",
            "You can make your own happiness.",
            "A stranger, is a friend you have not spoken to yet."
            ]

repeating = True
while repeating:
    #The way it should be done
    print(fortunes[randint(0, len(fortunes) - 1)])

    #The way you want it done
    #randomNumber = randint(0, len(fortunes) - 1)
    #if randomNumber == 0:
    #    print("A friend asks only for your time not your money.")
    #elif randomNumber == 1:
    #    print("Today it's up to you to create the peacefulness you long for.")
    
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
