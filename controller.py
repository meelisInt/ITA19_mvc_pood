import exceptions
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")

    def showItems(self):
        items = self.model.showItems()
        self.view.showItems(items)

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def deleteItem(self, name):
        try:
            self.model.deleteItem(name)
            self.view.deleteItem(name)
        except:
            self.view.noItemToDelete(name)

    def deleteAllItems(self):
        self.model.deleteAllItems()
        self.view.deleteAllItems()

    def updateItem(self, name, price, amount):
        try:
            self.model.updateItem(name, price, amount)
            self.view.updateItem(name)
            self.showItem(name)
        except:
            self.view.noItemToUpdateError(name)
            self.view.noItemError(name)

    def addFromStock(self, name, price, takeAmount):
        try:
            self.model.addFromStock(name, price, takeAmount)
            self.view.addFromStock(name, price, takeAmount)
        except:
            self.view.noItemError(name)
class Stock_Controller:
    def __init__(self, stock_model, stock_view):
        self.stock_model = stock_model
        self.stock_view = stock_view
    def addStockItem(self, name, price, amount):
        try:
            self.stock_model.addStockItem(name, price, amount)
            print("{} has been added!".format(name))
        except:
            print("Problem!")
    def showStockItems(self):
        stock_items = self.stock_model.showStockItems()
        self.stock_view.showStockItems(stock_items)

    def showStockItem(self, name):
        try:
            item = self.stock_model.showStockItem(name)
            self.stock_view.showStockItem(item)
        except:
            self.stock_view.noItemErrorStock(name)
    def deleteStockItem(self, name):
        try:
            self.stock_model.deleteStockItem(name)
            self.stock_view.deleteStockItem(name)
        except:
            self.stock_view.noStockItemToDelete(name)

    def deleteStockAllItems(self):
        self.stock_model.deleteStockAllItems()
        self.stock_view.deleteStockAllItems()

    def updateStockItem(self,name, price, amount):
        try:
            self.stock_model.updateStockItem(name, price, amount)
            self.stock_view.updateStockItem(name, price, amount)
        except:
            self.stock_view.noItemErrorStock(name)
    def addFromStock(self, name, price, takeAmount):
        try:
            self.model.addFromStock(name, price, takeAmount)
            self.view.addFromStock(name, price, takeAmount)
        except:
            self.view.noItemError(name)