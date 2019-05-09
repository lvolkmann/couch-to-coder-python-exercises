"""
Develop the following:
A class, ShoppingCart
-	Should be able to keep track of name and items contained
-	Method to print receipt
-	String rep of cart and number of unique items
-	Overload “-“ to remove item
-	Overload “+” to add item (no duplicates)
A class, Item
-	Keep track of name price and quantity
-	String rep of name, qty, and price
"""

class shoppingCart(object):

    def __init__(self, lst, name):
        self.items = lst
        self.name = name

    def printReceipt(self):
        for item in self.items:
            print('{:<20}{:<8}{}'.format( \
                item.name, item.quantity, item.subTotal()))

        print('Total',self.calcTotal())

    def calcTotal(self):
        total = 0

        for item in self.items:
            total += item.subTotal()
        
        return total
        
        
class Item(object):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subTotal(self):
        return self.price * self.quantity

w = Item("A Tire?", 175, 4)
x = Item("Empty Calories", .79, 2)
y = Item("Serious Mistake", .81, 2)
z = Item("Serious Mistake", .81, 1)
me = shoppingCart([x,y], "Landon")
#me + w
shoppingCart.printReceipt(me)

#me + z
#me - Item("A Tire?", 0, 0)
#me.printReceipt()

"""
>>>
Empty Calories		2	0.79
Serious Mistake		2	0.81
A Tire?	                4       175

Total: 703.2
Empty Calories		2	0.79
Serious Mistake		3	0.81

Total: 4.01"""
