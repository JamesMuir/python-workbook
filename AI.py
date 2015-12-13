#AI
import time
import calendar
import datetime

repeating = True
while repeating:
    #userInput = input("Enter question: ").lower()

    testString = "what date time show calendar"

    #Writes userInput to file 
    #logging = open('logging.txt', 'a')
    #logging.write(userInput + "\n")
    #logging.close()

    #Array of all possible questions and answers 
    answersAndResponses = [
     [['what', 'date'], ['print("Current date: {}".format(time.strftime("%d/%m/%Y")))']],   
     [['what', 'time'], ['print("Current time is: {}".format(time.strftime("%H:%M:%S")))']],
     [['show', 'calendar'], ['print(calendar.month(datetime.date.today().year, datetime.date.today().month))']] 
    ]

    for i in answersAndResponses:
        print(i)
        print()
        print(i[0])
        print()
        print(i[0][0])
        print(i[0][1])

    #print(answersAndResponses[0][0])
    #print(len(answersAndResponses))
    #print(answersAndResponses[0][1])
    #print(len(answersAndResponses[0]))

    #response = answersAndResponses[0][1][0]

    #print(response)
    
    #eval(response)

    #if userInput.find("what") >= 0 and userInput.find("date") >= 0:
    #    print("Current date: {}".format(time.strftime("%d/%m/%Y")))
    #if userInput.find("what") >= 0 and userInput.find("time") >= 0:
    #    print("Current time is: {}".format(time.strftime("%H:%M:%S")))
    #if userInput.find("show") >= 0 and userInput.find("calendar"):
    #    print(calendar.month(datetime.date.today().year, datetime.date.today().month))
    
    break
