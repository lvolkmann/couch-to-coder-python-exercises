"""
Given class Employee, create two child classes FullTime and Intern
Design the classes such that Interns may be assigned supervivsors (FullTime instances)
Overload the + operator to assign an Intern to a FullTime
Also implement fire, give_raise, and showInterns methods where applicable
"""

class Employee(object):

        ID_FACTORY = 0
        
        def __init__(self, xname):
                
                Employee.ID_FACTORY += 1
                self.ID = Employee.ID_FACTORY
                self.name = xname
                terminated = False
        def __str__(self):
                return "{}({})".format(self.name, self.ID)

#Tests
        
e1 = FullTime("John")
e2 = FullTime("Jack", 4000)
i1 = Intern("Jill")
i2 = Intern("Janice")
i3 = Intern("Jamie", 12)

print(e1)
print()
print(i2)

e1 + i1
i2 + e1

print("HELLO")
print(i2)

print(i1)
print(e1)
e1.showInterns()

i1.fire()
print(i1.terminated)
print(e1)
e1.showInterns()

