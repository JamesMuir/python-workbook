#IRRITATING PEOPLE [10]
def write(people):
    file = open("people.txt", "w")
    for i in people:
        file.write(i+" ")
    file.close()

def read():
    with open("people.txt") as f:
        fileContent = f.readlines()

    if len(fileContent) > 0:
        namesList = fileContent[0].split()

        return namesList
    
    else:
        return [""]
    
repeating = True
while repeating:
    gettingData = True
    while gettingData:
        print("Select Option \n1. View the list \n2. Remove a person from the list \n3. Add a person to the list\n")
        option = input("Enter 1, 2 or 3: ")
        if option == "1" or option == "2" or option == "3":
            print("Is the above correct?")
            while True:
                dataCorrect = input("Enter Y/N: ")
                if dataCorrect == "y":
                    gettingData = False
                    break
                elif dataCorrect == "n":
                    break
                
    names = read()
    if option == "1":
        for i in names:
            print(i)
    elif option == "2":
        for i in names:
            print(i)
        while True:
            nameToRemove = input("Please enter a name to remove: ")
            if nameToRemove in names:
                names.remove(nameToRemove)
                break
        
    elif option == "3":
        gettingName = True
        while gettingName:
            nameToAdd = input("Please enter a name to add: ")
            while True:
                print("Is this correct?")
                isNameCorrect = input("Enter Y/N: ").lower()
                if isNameCorrect == "y":
                    gettingName = False
                    break
                elif isNameCorrect == "n":
                    break
                
            names.append(nameToAdd)
            
    write(names)         
    print()
    while True:
        userRepeat = input("Do you want to repeat? \nEnter Y/N: ").lower()
        if userRepeat == "y":
            break
        elif userRepeat == "n":
            repeating = False
            break
        
