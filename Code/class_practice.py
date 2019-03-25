class shoppingCart(object):
    
    def __init__(self, xitems = [], xcustomer = "XxxxxX"):
        """tuple:xitem:(str: name, float: price)"""

        self.items = xitems
        self.customer = xcustomer
        self.total = 0

    def __str__(self):
        return "{} has {} items in their cart".format(self.customer, len(self.items))

    def __repr__(self):
        return "{} has {} items in their cart".format(self.customer, len(self.items))

    def __add__(self, item):
        self.items.append(item)

    def __sub__(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(i)

    def calcTotal(self):
        total = 0
        for item in self.items:
            total += item.calcSubTotal()
        self.total = total

    def printReceipt (self):
        for item in self.items:
            print(item)
        self.calcTotal()
        print()
        print("Total:", self.total)

class Item(object):
    
    def __init__(self, xname, xprice, xqty):
        self.name = xname
        self.price = xprice
        self.qty = xqty

    def __str__(self):
        return "{}\t\t{}\t{}".format(self.name, self.qty, self.price)

    def __repr__(self):
        return "{}\t\t{}\t{}".format(self.name, self.qty, self.price)
    
    def calcSubTotal(self):
        return self.price * self.qty
    def __eq__(self, item):
        if self.name == item.name:
            return True
        else:
            return False


x = Item("banana", .79, 2)
y = Item("banana", .81, 2)
me = shoppingCart([x,y], "landon")

