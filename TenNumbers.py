#TenNumbers
from commonFunctions import float_input

repeating = True
while repeating:
    numbers = []
    for i in range(10):
        numbers.append(float_input("Please enter a number: "))

    print(numbers)

    total = 0
    for i in range(10):
        total += numbers[i]
