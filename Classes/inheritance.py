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
class Square(Shape):
    
    def __init__(self, xlength, xcolor = "", xname = ""):
        Shape.__init__(self, xlength, xcolor, xname)
    def get_area(self):
        return self.length **2
    def get_perimeter(self):
        return self.length*4
    def __str__(self):
        return Shape.__str__(self) + '\n' + "Length : {} \nArea : {} \nPerimeter : {}".format(self.length, self.get_area(), self.get_perimeter())
    def __repr__(self):
        return Shape.__repr__(self) + '\n' + "Length : {} \nArea : {}\nPerimeter : {}".format(self.length, self.get_area(), self.get_perimeter())

class Circle(Shape):
    
    def __init__(self, xradius, xcolor = "", xname = ""):
        Shape.__init__(self, xradius, xcolor, xname)
    def get_area(self):
        return (self.length ** 2) * math.pi
    def get_perimeter(self):
        return self.length * 2 * math.pi
    def __str__(self):
        return Shape.__str__(self) + '\n' + "Radius : {} \nArea : {} \nPerimeter : {}".format(self.length, self.get_area(), self.get_perimeter())
    def __repr__(self):
        return Shape.__repr__(self) + '\n' + "Radius : {} \nArea : {}\nPerimeter : {}".format(self.length, self.get_area(), self.get_perimeter())

b = Square(5, "Blue", 'Bob the Square')
c = Circle(5, "Red", 'Sue the Circle')

print(b)
print()
print(c)

