#FIVE GAMER NAMES [3]
def AskForPlayerName():
    name = input("Please enter your name: ")
    return name
    
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        names = ["","","","",""]
        for i in range(5):
            names[i] = AskForPlayerName()

        for i in range(5):
            print(names[i], end=" ")

        print()
        while True:
            print("Is the above data correct?")
            inputRight = input("Enter Y/N: ").lower()
            if inputRight == "y":
                gettingData = False
                break
            elif inputRight == "n":
                break

    print()
    for i in range(5):
        print(names[i])

    while True:
        print("Do you want to repeat?")
        userRepeat = input("Enter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
              
            
