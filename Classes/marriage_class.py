"""
Write a class Person with member variables name and spouse
Name is the name of the person and spouse is a reference to another person
Overload the + operator such that person1 + person2 sets eachother as spouses
Overload the __str__ such that it returns the name of the person
Define a showPartner method to check your work
"""
class person:

    def __init__(self, xname):
        self.name = xname
        self.spouse = ""

    def __add__(self, p2):
        
        self.spouse = p2
        p2.spouse = self

    def __str__(self):
        return self.name

    def showPartner(self):
        print(self.spouse)


me = person("landon")
her = person("literally anyone please")
me + her

me.showPartner()
her.showPartner()
