#ENTER A BLEEDIN NUMBER [2]
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Error you inputed something that can't be converted into an int")
    except KeyboardInterrupt:
        print("Exiting")
        break
