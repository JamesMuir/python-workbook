#THREE STRIKES BATTLE TIME[5]
from random import randint

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        nameOne = input("Please enter the first name: ")
        nameTwo = input("Please enter the second name: ")

        print("You entered {} and {} as the two names.".format(nameOne,nameTwo))
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
        
    warriorOne = randint(30,35)     
    warriorTwo = randint(30,35)     

    print("{} has {} health and {} has {}.".format(nameOne,warriorOne,nameTwo,warriorTwo))
    

    for i in range(3):
        warriorOne -= randint(1,10)
        warriorTwo -= randint(1,10)
        if warriorOne > 0 and warriorTwo > 0:
            print("{} has {} health and {} has {} remaining.".format(nameOne,warriorOne,nameTwo,warriorTwo))
        elif warriorOne <= 0 and warriorTwo <= 0:
            print("Both warriors kill each other. ")
            break
        elif warriorOne <= 0:
            print("Warrior one dies.")
            break
        elif warriorTwo <= 0:
            print("Warrior two dies.")
            break
        else:
            print("ERROR")
            
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
