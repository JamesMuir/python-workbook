#THE FOOTBALL LEAGUE [7]
from commonFunctions import int_input

class Club:
    'Class which creates a new club with name and points'
    def __init__(self, name, points):
        global clubs
        self.name = name
        self.points = points
        clubs += [[name, points]]

clubs = []
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        nameOne = input("Enter the name of club one: ")
        pointsOne = int_input("Enter the number of points for club one: ")
        nameTwo = input("Enter the name of club two: ")
        pointsTwo = int_input("Enter the number of points for club two: ")
        nameThree = input("Enter the name of club three: ")
        pointsThree = int_input("Enter the number of points for club three: ")

        print("Club one: Name: {} Points: {}.".format(nameOne, pointsOne))
        print("Club two: Name: {} Points: {}.".format(nameTwo, pointsTwo))
        print("Club three: Name: {} Points: {}.".format(nameThree, pointsThree))
        
        while True:
            isInformationCorrect = input("Is the above information correct. Enter Y/N: ").lower()
            if isInformationCorrect == "y":
                gettingData = False
                ClubOne = Club(nameOne, pointsOne)
                ClubTwo = Club(nameTwo, pointsTwo)
                ClubThree = Club(nameThree, pointsThree)
                break
            elif isInformationCorrect == "n":
                break
            else:
                print("Enter Y/N.")
                print()

    clubsSorted = sorted(clubs, key=lambda  x:x[1])
    
    print(clubsSorted)
        
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

