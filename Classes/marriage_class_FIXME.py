"""
Write a class Person with member variables name and spouse
Name is the name of the person and spouse is a reference to another person
Overload the + operator such that person1 + person2 sets eachother as spouses
Overload the __str__ such that it returns the name of the person
Define a showPartner method to check your work
"""

me = person("landon")
her = person("literally anyone please")
me + her

me.showPartner()
her.showPartner()
