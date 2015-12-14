#The Collatz Sequence
def Collatz(number):
    if number == 1:
        print(number)
        return number
    elif number % 2 == 0:
        print(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)
        return (3 * number + 1)
    
repeating = True
while repeating:
    while True:
        try:
            number = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Enter a numerical value.")
        except:
            print("What did you do.")

    while number != 1:
        number = Collatz(number)
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    
