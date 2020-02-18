
inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(stuff):

    print('Inventory:')
    itemcount = 0
    for k, v in stuff.items():

        print(str(v)  +' '+ k)
        itemcount=itemcount + v

    print ("Total number of items: " + str(itemcount))
    
displayInventory(inventory)
