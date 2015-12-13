#HOW MANY MINUTES[2]
repeating = True

while repeating:
    print("Please enter the number of days and hours you want converted into minutes.")
    while True:
        try:
            numberOfDays = int(input("How many days: "))
            numberOfHours = int(input("How many hours: "))
        except ValueError:
            print("Enter a numerical value.")
        except:
            print("How did you manage to brake something this badly???")
            
