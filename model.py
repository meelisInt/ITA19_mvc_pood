import helpers


class Model_shop:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
    # show items
    def showItems(self):
        return helpers.showItems()
    # show item
    def showItem(self, name):
        return helpers.showItem(name)
    # delete item
    def deleteItem(self, name):
        helpers.deleteItem(name)
    # delete all items
    def deleteAllItems(self):
        helpers.deleteAllItems()
    # update item
    def updateItem(self, name, price, amount):
        helpers.updateItem(name, price, amount)

    def addFromStock(self, name, price, newAmount):
        helpers.addFromStock(name, price, newAmount)

class Stock_Model:
    # get stock data - [] of products
    def __init__(self, stock_items):
        self.items = stock_items
    # add item to items
    def addStockItem(self, name, price, amount):
        helpers.addStockItem(name, price, amount)
    # show items
    def showStockItems(self):
        return helpers.showStockItems()
    # show item
    def showStockItem(self, name):
        return helpers.showStockItem(name)
    # delete item
    def deleteStockItem(self, name):
        return helpers.deleteStockItem(name)
    # delete all items
    def deleteStockAllItems(self):
        return helpers.deleteStockAllItems()
    # update item
    def updateStockItem(self, name, price, amount):
        return helpers.updateStockItem(name, price, amount)