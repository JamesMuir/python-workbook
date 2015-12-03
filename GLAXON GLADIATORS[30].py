#Glaxon Gladiators 

#Importing modules 
import random 

#Player class
class player:
    def purchaseItems():
        global items
        global playerCredits
        
        print("Welcome to the Glaxon robot gladiator store. \nYou have %s credits remaining." %playerCredits)  
        print("Here are your options: ")
        #Prints out the list
        ListItems(items)
        print("Remember each item is one use only")
        
        while playerCredits > 0:
            print("Please enter the numer of the item you want to buy.")
            try:
                playerInput = int(input("Enter number: "))
            except ValueError:
                print("Enter a numerical value") 
            player.BuyItem(playerInput)

    def BuyItem(itemId):
        global items
        global playerCredits
        global playerItems

        try:
            #Check Player has enough credit for item
            if playerCredits < items[itemId][2]:
                print("Sorry you do not have enough credits left")
            else:
                playerCredits = playerCredits - items[itemId][2]
                playerItems.append(items[itemId][0])
                print("You have just bought %s" %items[itemId][1])
                print("You have %s credits remaining" %playerCredits)
                print()
                
        except IndexError:
            print("Enter a nubmer between 0 and 5.")
        
#AI class
class ai:
    def purchaseItems():
        global aiCredits
        
        while aiCredits > 0:
            ai.BuyItem(random.randint(0,5))

    def BuyItem(itemId):
        global items
        global aiCredits
        global aiItems

        try:
            #Check Player has enough credit for item
            if aiCredits < items[itemId][2]:
                #print("Sorry you do not have enough credits left")
                pass
            else:
                aiCredits = aiCredits - items[itemId][2]
                aiItems.append(items[itemId][0])
                #print("You have just bought %s" %items[itemId][1])
                #print("You have %s credits remaining" %aiCredits)
                #print()
                
        except IndexError:
            #print("Enter a nubmer between 0 and 5.")
            pass
        

#Start up script
def StartUp():
    global aiCredits
    global aiItems
    print("Welcome to Glaxon Gladiators")
    print("You must kit out a battle robot to fight the Glaxon robot")
    print()
    player.purchaseItems()
    ai.purchaseItems()
    print(aiCredits)
    print(aiItems)

#Fucntion which will print out the items in the inventory and format them - WIP
def ListItems(itemList):
    global items
    for row in itemList:
    # Loop over columns.
        for column in row:
            print(column, end=" ")
        print(end="\n")



#Items
#Name, cost, damage 
items = [
    [0, "Power Punch", 1, 1],
    [1, "Heat Missile", 2, 3],
    [2, "Plasma Punch", 4, 7],
    [3, "Force Field", 2, 10],
    [4, "Hydrogen Force Field", 3, 20],
    [5, "Nuke", 16, 30]
]

playerCredits = 20
playerItems = []
aiCredits = 20
aiItems = []

#Start of program
StartUp()

