#Imperial and metric convertor [2-5]
from commonFunctions import * #Custom file make sure it is available 

repeating = True
while repeating:
    print("""
1. KM to Miles
2. Miles to KM
3. KM to Meters
4. Meters to KM
5. Meters to CM
6. CM to Meters
7. Feet to Inches
8. Inches to Feet
9. CM to Inches
10. Inches to CM
""")

    choice = int_input("Please enter a number: ")

    if choice == 1:
        userInput = float_input("Enter number of KM: ")
        output = userInput * 0.621371
        print("{} KM is {} miles.".format(userInput, output))
    elif choice == 2:
        userInput = float_input("Enter number of Miles: ")
        output = userInput * 1.60934
        print("{} Miles is {} KM.".format(userInput, output))
    elif choice == 3:
        userInput = float_input("Enter number of KM: ")
        output = userInput * 1000
        print("{} KM is {} Meters.".format(userInput, output))
    elif choice == 4:
        userInput = float_input("Enter number of Meters: ")
        output = userInput / 1000
        print("{} Meters is {} KM.".format(userInput, output))
    elif choice == 5:
        userInput = float_input("Enter number of Meters: ")
        output = userInput * 100
        print("{} Meters is {} CM.".format(userInput, output))
    elif choice == 6:
        userInput = float_input("Enter number of CM: ")
        output = userInput / 100
        print("{} CM is {} Meters.".format(userInput, output))
    elif choice == 7:
        userInput = float_input("Enter number of Feet: ")
        output = userInput * 12
        print("{} Feet is {} Inches.".format(userInput, output))
    elif choice == 8:
        userInput = float_input("Enter number of Inches: ")
        output = userInput / 12
        print("{} Inches is {} Feet.".format(userInput, output))
    elif choice == 9:
        userInput = float_input("Enter number of CM: ")
        output = userInput / 2.54
        print("{} CM is {} Inches.".format(userInput, output))
    elif choice == 10:
        userInput = float_input("Enter number of Inches: ")
        output = userInput * 2.54
        print("{} Inches is {} CM.".format(userInput, output))
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
