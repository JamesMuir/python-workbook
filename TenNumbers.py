#TenNumbers
from commonFunctions import float_input

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

repeating = True
while repeating:
    numbers = []
    for i in range(10):
        numbers.append(None)
        while True:
            numbers[i] = float_input("Please enter number {}: ".format(i+1))
            if numbers[i] >= 0:
                break
            
    total = 0
    for i in range(10):
        total += numbers[i]

    numbersSorted = sorted(numbers)
    mean = total /10
    median = (numbersSorted[4] + numbersSorted[5])/2
    mode = mode(numbers)
    theRange = numbersSorted[9] - numbersSorted[0]

    print("The total is {}.".format(total))
    print("The mean is {}.".format(mean))
    print("The median is {}.".format(median))
    print("The mode is {}.".format(mode))
    print("The range is {}.".format(theRange))
    
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
