from tkinter import * 
from random import randint

def submit():
    name = nameBox.get()
    hairColour = hairColourBox.get()
    eyeColour = eyeColourBox.get()
    cannibalMessage(name, hairColour, eyeColour)

def cannibalMessage(userName, hairColour, eyeColour):
    message.set(responses[randint(0, len(responses)-1)].format(userName, hairColour, eyeColour))

    
responses = ["Hello, {} people with {} hair and {} eyes are very tasty in the cooking pot!",
            "Hello, {} people with {} hair and {} eyes are very tasty over the fire!",
            "Hello, {} people with {} hair and {} eyes smell horrible when set on fire!"
            ]

#Create the window
window = Tk()

#Gets first name
Label(window, text="Name: ").pack()
nameBox = Entry(window)
nameBox.pack()

#Gets hair colour 
Label(window, text="Hair Colour: ").pack()
hairColourBox = Entry(window)
hairColourBox.pack()

#Gets hair colour 
Label(window, text="Eye Colour: ").pack()
eyeColourBox = Entry(window)
eyeColourBox.pack()

#Submit button
submit = Button(window, text="Submit", width=15, command=submit)
submit.pack()

#Will display age
message = StringVar()
messageBox = Label(window, textvariable=message).pack()

mainloop()
