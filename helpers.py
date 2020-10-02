import exceptions
from product import Product


# repsresents shop structure
# list of Product type objects
items = []
stock_items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return items
# show item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))
# delete item
def deleteItem(name):
    global items
    isDeleted = False
    for item in items:
        # if the name is the same as we search
        if (item.getName() == name):
            items.remove(item)
            isDeleted = True
        else:
            continue
    if (isDeleted != True):
        raise exceptions.ItemNotExists("Not found {} item.".format(name))
# delete all items
def deleteAllItems():
    global items
    items.clear()
# update items price and amount
def updateItem(name, price, amount):
    global items
    isUpdated = False
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            # update item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    if (isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))

#**************stock*************
stock_items = []

def addStockItem(name, price, amount):
    global stock_items
    # create product with reqiure description
    stock_product = Product(name, price, amount)
    # control is item already exists
    if stock_product in stock_items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        stock_items.append(stock_product)

def showStockItems():
    global stock_items
    # control if items exists
    if len(stock_items) == 0:
        raise exceptions.ItemExists("List of items is empty")
    else:
        return stock_items

def showStockItem(name):
    global stock_items
    # control all items step by step
    for item in stock_items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item".format(name))

def deleteStockItem(name):
    global stock_items
    isDeleted = False
    for item in stock_items:
        # if the name is the same as we search
        if (item.getName() == name):
            stock_items.remove(item)
            isDeleted = True
        else:
            continue
    if (isDeleted != True):
        raise exceptions.ItemNotExists("Not found {} item.".format(name))
# delete all items
def deleteStockAllItems():
    global stock_items
    stock_items.clear()
# update items price and amount
def updateStockItem(name, price, amount):
    global stock_items
    isUpdated = False
    # control all items step by step
    for item in stock_items:
        # if the name is the same as we search
        if(item.getName() == name):
            # update item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    if (isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))

def addFromStock(name, price, takeAmount):
    global items
    global stockItems
    global updateItemStock
    global addItem

    for item in stock_items:
        # if the name matches our search
        if(item.getName() == name):
            newStockAmount = (item.getAmount() - takeAmount)
            item.setAmount(newStockAmount)
            continue
        else:
            continue
            raise exceptions.ItemNotExists("Item {} doesn't exist in stock".format(name))

    for thing in items:
        # if the name matches our search
        if (thing.getName() == name):
            totalAmount = thing.getAmount() + takeAmount
            thing.setPrice(price)
            thing.setAmount(totalAmount)
        else:
            product = Product(name, price, takeAmount)
            if product in items:
                print("Error: Item {} already exists".format(name))
            else:
                items.append(product)
            break
    for item in stock_items:
        if item.getAmount() <= 0:
            deleteStockItem(item.getName())