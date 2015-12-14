#TAX MAN[2]
repeating = True

while repeating:
    while True:
        amount = input("Enter the price: ")

        print("You entered {}.".format(amount))
        correct = input("Is this correct enter Y/n: ").lower()
        if correct == "y":
            break
        elif correct == "n":
            pass
        else:
            print("Enter Y/n.")
    
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    

