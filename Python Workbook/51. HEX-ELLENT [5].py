#HEX-ELLENT [5]
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        number = input("Please enter a 2 digit hex number or 8 bit binary number: ")
        if len(number) == 2:
            try:
                binaryNumber = bin(int(number, 16))
                while True:
                    print("You entered {}.".format(number))
                    isDataCorrect = input("Is this correct? Enter Y/N: ").lower()
                    
                    if isDataCorrect == "y":
                        gettingData = False
                        break
                    elif isDataCorrect == "n":
                        break
            except ValueError:
                print("Enter a valid hexadecimal number.")
                
        elif len(number) == 8:
            try:
                hexNumber = hex(int(number, 2))
                while True:
                    print("You entered {}.".format(number))
                    isDataCorrect = input("Is this correct? Enter Y/N: ").lower()
                    
                    if isDataCorrect == "y":
                        gettingData = False
                        break
                    elif isDataCorrect == "n":
                        break
            except ValueError:
                print("Enter a valid binary number.")
    

    if len(number) == 2:
        print("{} in binary is {}.".format(number, binaryNumber[2:]))
        
    elif len(number) == 8:
        print("{} in hex is {}.".format(number, hexNumber[2:]))

    print()
    while True:
        print("Do you want to repeat?")
        repeat = input("Enter Y/N: ").lower()
        if repeat == "y":
            break
        elif repeat == "n":
            repeating = False
            break
