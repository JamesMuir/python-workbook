#THREE NUMBER LOTTERY [7]
from random import randint
from commonFunctions import int_input

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        numbers = []
        print("Please enter three different numbers between.")
        for i in range(3):
            numbers.append(None)
            while True:
                numbers[i] = int_input("Please enter number {}: ".format(i+1))
                if numbers[i] >= 1 and numbers[i] <= 10:
                    break
                    
        
        if numbers[0] in numbers[1:]:
            print("Please make sure the numbers are different.")
        elif numbers[1] == numbers[0] or numbers[1] == numbers[2]:            
            print("Please make sure the numbers are different.")
        elif numbers[2] in numbers[:2]:
            print("Please make sure the numbers are different.")
        else:
            print("You entered {}.".format(numbers))
            while True:
                print("Is this correct?")
                isCorrect = input("Enter Y/N: ").lower()
                if isCorrect == "y":
                    gettingData = False
                    break
                elif isCorrect == "n":
                    break
        
    while True:
        lottery = []
        for i in range(3):
            lottery.append(randint(1,10))
        if lottery[0] in lottery[1:]:
            pass
        elif lottery[1] == lottery[0] or lottery[1] == lottery[2]:
            pass
        elif lottery[2] in lottery[:2]:
            pass
        else:
            break

    if numbers == lottery:
        print("Well done you won the lottery.")
        print(numbers)
        print(lottery)
    else:
        print("Sorry you lost.")
        print(numbers)
        print(lottery)

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
