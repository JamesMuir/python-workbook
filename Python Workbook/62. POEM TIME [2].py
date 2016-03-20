#POEM TIME [2]
repeating = True
while repeating:
    gettingData = True
    poemLines = [""]
    poemLine = 0
    while gettingData:
        poemLines[poemLine] = input("Enter a line {} poetry: ".format(poemLine + 1))

        #Sees if the line is right and if the user wants to add another 
        while True:
            print("Is the above line correct?")
            isLineCorrect = input("Enter Y/N: ").lower()
            
            if isLineCorrect == "y":
                print("Do you want to add another line: ")
                userWantToAddAnotherLine = input("Enter Y/N: ").lower()
                if userWantToAddAnotherLine == "y":
                    poemLines.append("")
                    poemLine += 1
                    break
                elif userWantToAddAnotherLine == "n":
                    gettingData = False
                    break
                
            elif isLineCorrect == "n":
                break

    file = open("poem.txt","w")
    for i in poemLines:
        file.write(i+"\n")
    file.close()

    print()
    print("Do you want to repeat?")
    while True:
        userRepeat = input("Enter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
