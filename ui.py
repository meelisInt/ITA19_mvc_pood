# ui.py

# import classes and files
from product import Product
from shop import Shop
from stock import Stock
from controller import Controller
from model import *
from view import *
from controller import Stock_Controller


# create products
bread = Product("bread", 0.80, 10)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 5)

# create shop and add products to shop
shop = Controller(Model_shop(Shop()), View())
#shop.addItem("bread", 0.80, 10)
#shop.addItem("milk", 0.50, 50)
#shop.addItem("wine", 5.60, 5)

# show items
#shop.showItems()
# show item
#shop.showItem("wine")

#shop.updateItem("milk", 1, 10)

#shop.deleteItem("milk")

#shop.deleteAllItems()

stock = Stock_Controller(Stock_Model(Stock()), Stock_View())

stock.addStockItem("muna", 0.5, 50)
stock.addStockItem("piim", 2, 20)
#shop.showItems()
stock.showStockItems()
#shop.addItem("milk", 0.50, 50)
stock.updateStockItem("muna", 1, 100)
shop.addItem("muna", 1, 20)
#shop.addItem("milk", 0.50, 50)
shop.addFromStock("muna", 1, 100)
#shop.addItem("milk", 0.50, 50)
shop.showItems()

#stock.showStockItem("muna")
#stock.showStockItems()
#stock.showStockItem("muna")
