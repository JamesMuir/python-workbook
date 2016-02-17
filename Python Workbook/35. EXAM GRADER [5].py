#EXAM GRADER [5]
from commonFunctions import float_input

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        while True:
            examScore = float_input("Please enter the exam score between 0 and 100: ")      
            if examScore >= 0 and examScore <= 100:
                break

        print("You selected an exam score of {}.".format(examScore))
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

    if examScore >= 80:
        print("Grade A.")
    elif examScore >= 70 and examScore < 80:
        print("Grade B")
    elif examScore >= 55 and examScore < 70:
        print("Grade C")
    elif examScore < 54:
        print("Fail")
    else:
        print("Error")
        
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
