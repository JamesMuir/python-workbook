#AI
import time
import calendar
import datetime

repeating = True
while repeating:
    userInput = input("Enter question: ").lower()
    logging = open('logging.txt', 'a')
    logging.write(userInput + "\n")
    logging.close()
    if userInput.find("what") >= 0 and userInput.find("date") >= 0:
        print("Current date: {}".format(time.strftime("%d/%m/%Y")))
    if userInput.find("what") >= 0 and userInput.find("time") >= 0:
        print("Current time is: {}".format(time.strftime("%H:%M:%S")))
    if userInput.find("show") >= 0 and userInput.find("calendar"):
        print(calendar.month(datetime.date.today().year, datetime.date.today().month))
