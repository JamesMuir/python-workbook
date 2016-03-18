#SMALLEST AND LARGEST [4]
from commonFunctions import int_input

def largest(numbers):
    numbersSorted = sorted(numbers)
    return numbersSorted[-1]

def smallest(numbers):
    numbersSorted = sorted(numbers)
    return numbersSorted[0]

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        numbers = [0,0,0]
        for i in range(3):
            numbers[i] = int_input("Enter number {}: ".format(i+1))
        
        for i in range(3):
            print(numbers[i], end=" ")
        print()
        print("Is this correct?")
        while True:
            dataCorrect = input("Enter Y/N: ").lower()
            if dataCorrect == "y":
                gettingData = False
                break
            elif dataCorrect == "n":
                break

    print("The smallest number is {}.".format(smallest(numbers)))
    print("The largest number is {}.".format(largest(numbers)))
            
    print()
    while True:
        print("Do yo want to repeat?")
        userRepeat = input("Enter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        
    
