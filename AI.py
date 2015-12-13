#AI
import time
import calendar
import datetime

def setUp():
    while True:
        name = input("Please enter a name: ")
        
        print(Your)
        
    information = open('information.txt', 'w')
    

repeating = True
while repeating:
    userInput = input("Enter question: ").lower()

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
     [['how', 'are', 'you'], ['print("Fine thanks.")']],
     [['setup'], ['']]
    ]

    for i in answersAndResponses:
        if userInput.find(i[0][0]) >= 0 and userInput.find(i[0][1]) >= 0 and userInput.find(i[0][2]) >= 0:
            eval(i[1][0])

