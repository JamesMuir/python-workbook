#IRRATATING PARROT[1]
while True:
    name = input("Please enter name: ")
    print("Your name is %s." %name)

    age = input("Please enter age: ")
    print("Your age is %s." %age)

    question = input("Please enter the correct word to brake out of the never ending loop: ")
    if question == "word":
        break
    else:
        print("You are a failure.")
