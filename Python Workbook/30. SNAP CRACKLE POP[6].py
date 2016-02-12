from random import randint

repeating = True
while repeating:
    words = [["snap"], ["crackle"], ["pop"]]
    wordsRandom = []

    # Places the words in a random order 
    totalWords = len(words) 
    wordsLeft = totalWords - 1
    for i in range(totalWords):
        wordsRandom += [words[randint(0,wordsLeft)]]
        words.remove(wordsRandom[i])
        wordsLeft -= 1

    # Gets the users three answers 
    gettingData = True
    while gettingData:
        guesses = []

        for i in range(3):
            guesses.append("")
            while True:
                guesses[i] = (input("Please enter a guess for word {}: ".format(i+1)).lower())
                if [guesses[i]] in wordsRandom:
                    break
                
                
        while True:
            print()
            isInformationCorrect = input("Is the above information correct. Enter Y/N: ").lower()
            if isInformationCorrect == "y":
                gettingData = False
                break
            elif isInformationCorrect == "n":
                break
            else:
                print("Enter Y/N.")
                print()

    # Works out how many the user got right 
    totalRight = 0
    for i in range(len(wordsRandom)):
        if wordsRandom[i] == [guesses[i]]:
            totalRight += 1

    print(totalRight)
    
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
