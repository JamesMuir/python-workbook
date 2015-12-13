#AI
import time
import calendar
import datetime

def setUp():
    global name
    
    notSetUp = True
    while notSetUp:
        name = input("Please enter a name: ")
        print()
        print("Your name is {}.".format(name))

        while True:
            x = input("Is the above information correct. Enter Y/n: ").lower()
            if x == "y":
                notSetUp = False
                break
            elif x == "n":
                break
            else:
                print("Enter a valid input.")
        
    information = open('information.txt', 'w')
    information.write(name + "\n")
    information.close()

def read():
    global name
    
    information = open('information.txt', 'r')
    name = information.readline()
    information.close()
    

print("To perform a set up enter setup. To read from the file enter read.")

repeating = True
while repeating:
    global name
    userInput = input("Enter question or command: ").lower()

    #Writes userInput to file 
    logging = open('logging.txt', 'a')
    logging.write(userInput + "\n")
    logging.close()

    #Gets user information
    #information = open('information.txt', 'w')
    

    #Array of all possible questions and answers 
    answersAndResponses = [
     [['what', 'date', ''], ['print("Current date: {}".format(time.strftime("%d/%m/%Y")))']],   
     [['what', 'time', ''], ['print("Current time is: {}".format(time.strftime("%H:%M:%S")))']],
     [['show', 'calendar', ''], ['print(calendar.month(datetime.date.today().year, datetime.date.today().month))']],
     [['how', 'are', 'you'], ['print("Fine thanks {}".format(name))']],
     [['setup', '', ''], ['setUp()']],
     [['read', '', ''], ['read()']]
    ]
    
    if userInput == "exit":
        repeating = False
    else:
        for i in answersAndResponses:
            if userInput.find(i[0][0]) >= 0 and userInput.find(i[0][1]) >= 0 and userInput.find(i[0][2]) >= 0:
                eval(i[1][0])

