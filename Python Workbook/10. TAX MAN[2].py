#TAX MAN[2]
repeating = True

while repeating:
    while True:
        try:
            amount = float(input("Enter the price: "))
        except ValueError:
            print("Enter a numerical value")
        except:
            print("You did what?")
        
        print("You entered {}.".format(amount))
        correct = input("Is this correct enter Y/n: ").lower()
        if correct == "y":
            break
        elif correct == "n":
            pass
        else:
            print("Enter Y/n.")

    tax = amount * 0.2
    total = tax + amount
    print("The total tax is {}. \nThe total with out tax is {}. \nThe total with tax is {}.\n".format(tax, amount, total))
    
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")


    

