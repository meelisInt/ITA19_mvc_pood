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

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop do no not consist item {}".format(name))
        print("============================")
    # delete item
    def deleteItem(self, name):
        print("Deleting {} item.".format(name))
        print("Item {} is deleted.".format(name))
    # delete all items
    def deleteAllItems(self):
        print("All items have been deleted.")
    # updating item
    '''def updateItem(self, name, old_price, old_amount, new_price, new_amount):
        print("{} has been updated".format(name))
        if(old_price != new_price):
            print("Price has been changed from {} to {}".format(old_price, new_price))
        if(old_amount != new_amount):
            print("Amount has been changed from {} to {}".format(old_amount, new_amount))'''