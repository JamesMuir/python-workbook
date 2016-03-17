#WHAT IS IN A NAME? [2]
def nameComment(name):
    nameUpper = name.upper()

    if nameUpper == "JIM":
        print("All people called Jim suck.")
    elif nameUpper == "SALLY":
        print("All people called Sally are ginger.")
    elif nameUpper == "MARY":
        print("All people called Mary are potatos.")
    elif nameUpper == "KIM":
        print("All people called Kim are Kardishians.")
    else:
        print("People called {} are meh.".format(nameUpper))
    
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        name = input("Please enter name: ")

        print()
        while True:
            print("You entered {}.".format(name))
            isDataCorrect = input("Is this correct? \nEnter Y/N: ").lower()

            if isDataCorrect == "y":
                gettingData = False
                break
            elif isDataCorrect == "n":
                break

    nameComment(name)
    
    print()
    while True:
        print("Do you want to repeat?")
        repeat = input("Enter Y/N: ").lower()
        if repeat == "y":
            break
        elif repeat == "n":
            repeating = False
            break
