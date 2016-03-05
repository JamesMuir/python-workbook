#47 CURRENCY CONVERTOR [4+2]
from commonFunctions import int_input, float_input

operations = [1.42, 0.7, 1.29, 0.77, 0.91, 1.1]

repeating = True
while repeating:
    gettingOperation = True
    while gettingOperation:
        print("""
1. British Pound Sterling to US Dollars
2. US Dollars to British Pound Sterling
3. British Pound Sterling to Euro
4. Euro to British Pound Sterling
5. US Dollar to Euro
6. Euro to Us Dollar 
""")
        
        operation = int_input("Please enter a number between one and six: ")

        while True:
            if operation >= 1 and operation <= 6:
                print("You selected operation {}.".format(operation))
                userRepeat = input("Is the above correct? \nEnter Y/N: ").lower()
                if userRepeat == "y":
                    gettingOperation = False
                    break
                elif userRepeat == "n":
                    break
            else:
                break

    gettingAmount = True
    while gettingAmount:
        if operation == 1 or operation == 3:
             amount = float_input("Enter the amount of pounds: ")
        elif operation == 2 or operation == 5:
            amount = float_input("Enter the amount of dollars: ")
        elif operation == 4 or operation == 6:
            amount = float_input("Enter the amount of euros: ")

        while True:
            print("The amount selected is {}.".format(amount))
            isAmountCorrect = input("Is this correct. Enter Y/N: ").lower()
            if isAmountCorrect == "y":
                gettingAmount = False
                break
            elif isAmountCorrect == "n":
                break

        
    output = amount * operations[operation - 1]

    if operation == 1 or operation == 6:
        print("The total is {} dollars.".format(output))
    elif operation == 2 or operation == 4:
        print("The total is {} pounds.".format(output))
    elif operation == 3 or operation == 5:
        print("The total is {} euros.".format(output))

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


