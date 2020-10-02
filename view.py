class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")
    # show item
    def showItem(self, item):
        print("Shop item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
        print("---------------------------")
        print("============================")

    def ListEmpty(self):
        print("============================")
        print("The list is empty.")
        print("============================")
    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop do no not consist item {}".format(name))
        print("============================")
    # delete item
    def deleteItem(self, name):
        print("Item {} has been deleted.".format(name))
    # delete all items
    def deleteAllItems(self):
        print("All items have been deleted.")
    # update item
    def updateItem(self, name):
        print("Shop item {} is updated.".format(name))
        print("============================")
     # no item to update error
    def noItemToUpdateError(self, name):
        print("============================")
        print("Not possible to update item {}".format(name))
        print("============================")
    def noItemToDelete(self, name):
        print("Failed to delete {}, item doesn't exist.".format(name))

    def addFromStock(self, name, price, newAmount):
        print("============================")
        print("Item {} is now in the shop under the price of {} and under the amount of {}".format(name, price,
                                                                                                   newAmount))
        print("============================")

class Stock_View:
    def showStockItems(self, stock_items):
        print("Stock items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in stock_items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")
    def noItemErrorStock(self, name):
        print("============================")
        print("Stock does not consist item {}".format(name))
        print("============================")
    def showStockItem(self, item):
        print("Stock item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
        print("---------------------------")
        print("============================")

    def ListEmptyStock(self):
        print("============================")
        print("The list is empty.")
        print("============================")

    def deleteStockItem(self, name):
        print("Item {} has been deleted.".format(name))
        # delete all items

    def deleteStockAllItems(self):
        print("All items have been deleted.")
        # update item

    def updateStockItem(self, name, price, amount):
        print("============================")
        print("Item {} now has a price of {} and there is {} of it.".format(name, price, amount))
        print("============================")

    def noStockItemToUpdateError(self, name):
        print("============================")
        print("Not possible to update item {}".format(name))
        print("============================")

    def noStockItemToDelete(self, name):
        print("Failed to delete {}, item doesn't exist.".format(name))