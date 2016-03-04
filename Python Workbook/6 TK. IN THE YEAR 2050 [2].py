#6 TK. IN THE YEAR 2050 [2]
from datetime import date
from tkinter import * 

def submit():
    firstName = firstNameBox.get()
    surname = surnameBox.get()
    age = int(ageBox.get())
    getAge(age)
    
def getAge(age):
    ageIn2050 = 2050 - date.today().year + age
    displayAge(ageIn2050)
    
def displayAge(ageIn2050):
    ageIn2050Display.set("Your age in 2050 will be {}".format(ageIn2050))

#Create the window
window = Tk()

#Gets first name
Label(window, text="First Name: ").pack()
firstNameBox = Entry(window)
firstNameBox.pack()

#Gets surname
Label(window, text="Surname: ").pack()
surnameBox = Entry(window)
surnameBox.pack()

#Gets age
Label(window, text="Age: ").pack()
ageBox = Entry(window)
ageBox.pack()

#Will display age
ageIn2050Display = StringVar()
ageIn2050Box = Label(window, textvariable=ageIn2050Display).pack()

submit = Button(window, text="Submit", width=15, command=submit)
submit.pack()

mainloop()
