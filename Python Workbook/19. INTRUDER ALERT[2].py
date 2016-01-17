#INTRUDER ALERT[2]

secretWordOne = "potato"
secretWordTwo = "tomato"

repeating = True
while repeating:
    answerOne = input("Enter word one: ")
    answerTwo = input("Enter word two: ")

    if secretWordOne == answerOne and secretWordTwo == answerTwo:
        print("Secret message.")        
    else:
        print("Passwords incorrect.")
    
    while True:
        userRepeat = input("\nDo you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            print()
            break
        elif userRepeat == "n":
            repeating = False
            break
        else:
            print("Enter valid input.")
