#WHAT IS IN A NAME? [2]
def nameComment(name):
    nameUpper name.upper()

    if nameUpper == "JIM":
        print("All people called Jim suck.")
    elif nameUpper == "SALLY":
        print("All people called Sally are ginger.")
    elif nameUpper == "MARY":
        print("All people called Mary are potatos.")
    elif nameUpper == "KIM":
        print("All people called Kim are Kardishians.")

repeating = True
while repeating:
    gettingData = True
    while gettingData:
        name = input("")
