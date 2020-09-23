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
            print("Failed to delete item.")
    def deleteAllItems(self):
        items = self.model.deleteAllItems()
        self.view.deleteAllItems()

    '''def updateItem(self, name, price, amount):
        if (price <= 0):
            print("Price must be higher than 0")
        elif (amount <= 0):
            print("Amount must be higher than 0")
        else:
            old_product = self.model.showItem(name)
            self.model.updateItem(name, price, amount)
            self.view.updateItem(name, old_product['price'], old_product['amount'], price, amount)'''