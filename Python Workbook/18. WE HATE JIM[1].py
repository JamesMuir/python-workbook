#WE HATE JIM[1]
repeating = True
while repeating:
    name = input("What is your name: ").lower()

    if name == "jim":
        print("Your in idiot Jim.")
        print()
    else:
        print("Your alright {}.".format(name))
        print()
        
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            print()
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
