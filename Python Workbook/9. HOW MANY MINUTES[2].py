#HOW MANY MINUTES[2]
repeating = True

while repeating:
    print("Please enter the number of days and hours you want converted into minutes.")
    while True:
        try:
            numberOfDays = int(input("How many days: "))
            numberOfHours = int(input("How many hours: "))
            break
        except ValueError:
            print("Enter a numerical value.")
        except:
            print("How did you manage to brake something this badly???")

    numberofMinutes =(numberOfDays * 24 * 60) + (numberOfHours * 60)

    print("The number of minutes is {}.".format(numberofMinutes))

    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    
