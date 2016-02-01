#NUMBER 15 BLOWS THE DEATH STAR[5]
from commonFunctions import int_input

missileTarget = 15

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        while True:
            attempts = int_input("Please enter a number between one and six of attempts you want: ")
            if attempts >= 1 and attempts <= 6:
                break
            
        print("You selected {} attempts.".format(attempts))
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
                    
    for i in range(attempts):
        while True:
            guess = int_input("Please enter a number between one and twenty to blow up the death star: ")
            if guess >= 1 and guess <= 50:
                break
        if guess == missileTarget:
            print("Well done you hit it.")
            break
        else:
            print("Missed")
        
            
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
