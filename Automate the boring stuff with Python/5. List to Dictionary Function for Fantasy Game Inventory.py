#List to Dictionary Function for Fantasy Game Inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
    
def addToInventory(inventory, addedItems):
    for key in addedItems:
        if key in inventory.keys() == True:
            print("Yea")
        print(key)
        #print(inventory[key])
        
inv  = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coins', 'ruby']
inv = addToInventory(inv, dragonLoot)
#displayInventory(inv)
#print(inv)
