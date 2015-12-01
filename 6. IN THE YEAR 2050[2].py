#IN THE YEAR 2050[2]
import datetime
repeating = True

while repeating:
    firstName = input("Please enter your first name: ")
    surname = input("Please enter your last name: ")
    while True:
        try:
            age = int(input("Please enter you age: "))
            break
        except ValueError:
            print("Please enter a numerical number.")

    ageIn2050 = 2050 - datetime.date.today().year + age
    print("Hello %s %s in 2050 you will be %s." %(firstName, surname, ageIn2050))

    while True:
        userRepeat = input("Do you wat to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    
