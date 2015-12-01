#Glaxon Gladiators 

#Importing modules 
import random 
#import enum


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
            playerInput = int(input("Enter number: "))
            BuyItem(playerInput)

#Start up script
def StartUp():
    print("Welcome to Glxon Gladiators")
    print("You must kit out a battle robot to fight the Glaxon robot")
    player.purchaseItems()
    


#Fucntion which will print out the items in the inventory and format them - WIP
def ListItems(itemList):
    global items
    for row in itemList:
    # Loop over columns.
        for column in row:
            print(column, end=" ")
        print(end="\n")

#Allows the purchace of items buy passing the id of the item 
def BuyItem(itemId):
    global items
    global playerCredits
    global playerItems
        
    #Check Player has enough credit for item
    if playerCredits < items[itemId][2]:
        print("Sorry you do not have enough credits left")
    else:
        playerCredits = playerCredits - items[itemId][2]
        playerItems.append(items[itemId][0])
        print("You have just bought %s" %items[itemId][1])
        print("You have %s credits remaining" %playerCredits)
        print()

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

