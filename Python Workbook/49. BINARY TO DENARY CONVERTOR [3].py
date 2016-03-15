#BINARY TO DENARY CONVERTOR [3]
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        dataValid = True
        binaryNumber = input("Please enter an 8bit binary number: ")
        if len(binaryNumber) == 8:
            for i in binaryNumber:
                if i == "0" or i == "1":
                    pass
                else:
                    dataValid = False
        else:
            dataValid = False
        
        if dataValid == True:
            while True:
                print("You entered {}.".format(binaryNumber))
                isDataCorrect = input("Is this correct? Enter Y/N: ").lower()
                
                if isDataCorrect == "y":
                    gettingData = False
                    break
                elif isDataCorrect == "n":
                    break
                
    denaryNumber = int(binaryNumber, 2)

    print("{} in denary is {}.".format(binaryNumber, denaryNumber))

    print()
    while True:
        print("Do you want to repeat?")
        repeat = input("Enter Y/N: ").lower()
        if repeat == "y":
            break
        elif repeat == "n":
            repeating = False
            break
        
