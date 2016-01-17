#THREE FISHY QUESTIONS[2]

repeating = True
while repeating:
    gettingData = True
    numberRight = 0
    while gettingData:
        while True:
            answerOne = input("What is the most type of fish eaten in the US? Is it shrimp, salmon or canned tuna: ").lower()
            if answerOne == "shrimp" or answerOne == "salmon" or answerOne == "canned tuna":
                break
            else:
                print("Enter on of the three options.")

        while True:
            answerTwo = input("Are starfish fish? Enter Y/N: : ").lower()
            if answerTwo == "y" or answerTwo == "n":
                break
            else:
                print("Enter Y/N.")

        while True:
            answerThree = input("What is the fastest type of fish? Is it sailfish, sharks, pupfish or anableps: ").lower()
            if answerThree == "sailfish" or answerThree == "sharks" or answerThree == "pupfish" or answerThree == "anableps":
                break
            else:
                print("Enter on of the three options.")

        print()
        print("")
        print()
        while True:
            isInformationCorrect = input("Is the above information correct. Enter Y/N: ").lower()
            if isInformationCorrect == "y":
                gettingData = False
                break
            elif isInformationCorrect == "n":
                break
            else:
                print("Enter Y/N.")
                print()

        if answerOne == "shrimp":
            numberRight += 1
            
        if answerTwo == "n":
            numberRight += 1

        if answerThree == "sailfish":
            numberRight += 1
