"""
Write two child classes, square and circle, that inherit from the given class shape
    - Have them inherit all the Shape member variables
    - Write get_area and get_perimeter methods unique to each child class
    - Override the __str__ and __repr__ methods to include area and perimeter
"""
import math

class Shape(object):
    
    def __init__(self, xlength, xcolor = "", xname = ""):
        self.length = xlength
        self.color = xcolor
        self.name = xname
    def __str__(self):
        return "Name : {} \nColor : {}".format(self.name, self.color)
    def __repr__(self):
        return "Name : {} \nColor : {}".format(self.name, self.color)    


b = Square(5, "Blue", 'Bob the Square')
c = Circle(5, "Red", 'Sue the Circle')

print(b)
print()
print(c)

