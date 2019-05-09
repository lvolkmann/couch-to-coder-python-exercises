"""Given the classes and calls below, predict the output of the following"""
class someClass:

	def __init__(self, name):
		self.name = name
	def __str__(self):
		return "{} the Mighty".format(self.name)

class someChildClass(someClass):

	def __init__(self, name):
		someClass.__init__(self, name)
	def __str__(self):
		return "I am a child of " + someClass.__str__(self)

Tim = someClass("Tim")
Agamemnon = someChildClass("Tim")

print(Tim)
print(Agamemnon)

"""Tim the Mighty
I am a child of Tim the Mighty"""

x = someClass("x")
y = someClass("x")
z = someChildClass("x")
a = x

print(x == y)
print(a == x)
print(x.name == y.name)
print(isinstance(x, someClass))
print(isinstance(z, someClass))
print(issubclass(someChildClass, someClass))

"""
False
True
True
True
True
True
"""
