#WORD MUDDLE [2]
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        wordOne = input("Please enter the first word: ")
        wordTwo = input("Please enter the second word: ")
        
        print("You entered {} and {}. Is this correct?".format(wordOne, wordTwo))
        while True:
            isDataCorrect = input("Enter Y/N: ").lower()
            if isDataCorrect == "y":
                gettingData = False
                break
            elif isDataCorrect == "n":
                break
                
    wordOne = (wordOne.strip()).upper()
    wordTwo = (wordTwo.strip()).lower()


    print(wordOne[1])
    print(wordTwo[2])

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

    

   
    
