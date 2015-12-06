#Multiplier[2]
repeating = True

while repeating:
    while True:
        try:
            variableOne = int(input("Please enter an integer: "))
            variableTwo = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    while True:
        print("Do you want to add or multiply?")
        addOrMultiply = input("Enter A or M: ").lower()
        if addOrMultiply == "a":
            variableTotal = variableOne + variableTwo
            print("{} + {} = {}".format(variableOne, variableTwo, variableTotal))
            break
        elif addOrMultiply == "m":
            variableTotal = variableOne * variableTwo
            print("{} * {} = {}".format(variableOne, variableTwo, variableTotal))
            break
        else:
            pass
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    
