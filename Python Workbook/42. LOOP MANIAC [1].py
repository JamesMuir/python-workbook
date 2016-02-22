#LOOP MANIAC [1]
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        print("Do you want to go to one or two million?")
        oneOrTwo = input("Please enter 1 or 2: ").lower()
        if onOrTwo == "1" or onOrTwo = "one":
            upTo = 1000000
        elif onOrTwo == "2" or onOrTwo = "two":
            upTo = 2000000
                    
    print()
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
