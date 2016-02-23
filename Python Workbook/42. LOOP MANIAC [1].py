#LOOP MANIAC [1]
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        print("Do you want to go to one or two million?")
        oneOrTwo = input("Please enter 1 or 2: ").lower()
        if oneOrTwo == "1" or oneOrTwo == "one":
            upTo = 1000001
        elif oneOrTwo == "2" or oneOrTwo == "two":
            upTo = 2000001


        for i in range(upTo):
            print(i)
        
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
