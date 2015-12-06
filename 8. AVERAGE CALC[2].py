#AVERAGE CALC[2]
repeating = True

while repeating:
    counter = 0
    numbers = [0, 0, 0, 0, 0]
    while counter < 5:
        try:
            numbers[counter] = float(input("Enter a value: "))
            counter +=1
        except ValueError:
            print("Enter a numerical value")
        except:
            print("What the hell did you do??")
    
    #Work out the average
    numbersTotal = 0
    for i in numbers:
        numbersTotal += i

    numbersAverage = numbersTotal / 5
    print("The average is {}.".format(numbersAverage))

    #Works out the sum of the first two numbers and then subtracts a third
    weirdNumber = numbers[0] * numbers[1] - numbers[3]
    print("The sum of the first two numbers minus the third is {}.".format(weirdNumber))
    
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
    

