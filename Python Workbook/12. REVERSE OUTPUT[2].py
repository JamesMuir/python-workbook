#REVERSE OUTPUT[2]
repeating = True
while repeating:
    letters = ["","","","",""]
    for x in range(0,5):
        letters[x] = input("Please enter a letter: ")

    for x in range (1,6):
        print(letters[-x])

   while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
