#AI
import time

repeating = True
while repeating:
    userInput = input("Enter question: ").lower()
    if userInput.find("what") >= 0 and userInput.find("date") >= 0:
        print("Current date: {}".format(time.strftime("%d/%m/%Y")))
    if userInput.find("what") >= 0 and userInput.find("time") >= 0:
        print("Current time is: {}".format(time.strftime("%H:%M:%S")))
