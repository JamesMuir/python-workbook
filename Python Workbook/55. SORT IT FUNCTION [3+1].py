from random import randint

#SORT IT FUNCTION [3 + 1]
def numberSort(numberOne, numberTwo, numberThree):
    numbers = [numberOne, numberTwo, numberThree]    
    numbers.sort()

    return numbers 

repeating = True
while repeating:
    print(numberSort(randint(1,1000),randint(1,1000), randint(1,1000)))

    print()
    while True:
        print("Do you want to repeat.")
        userWantToReapeat = input("Enter Y/N: ").lower()
        if userWantToReapeat == "y":
            break
        elif userWantToReapeat == "n":
            repeating = False
            break
    
