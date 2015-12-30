#PAY CALC[2]
from commonFunctions import *

repeating = True 
while repeating:
    gettingData = True
    while gettingData:
        hourlyPay = float_input("Enter the hourly wage: £")
        weekOne = float_input("Enter the hours worked in week one: ")
        weekTwo = float_input("Enter the hours worked in week two: ")
        weekThree = float_input("Enter the hours worked in week three: ")
        weekFour= float_input("Enter the hours worked in week four: ")
        print()
        while True:            
            informationCheck = input("Is the above information correct? Enter Y/N: ").lower()
            print()
            if informationCheck == "y":
                gettingData = False
                break
            elif informationCheck == "n":
                break
            else:
                print("Enter Y/N.")

    monthlyPay = hourlyPay * (weekOne + weekTwo + weekThree + weekFour)
    print("The monthly pay is £{}.".format(monthlyPay))
    
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
