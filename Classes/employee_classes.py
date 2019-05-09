class Employee(object):

        ID_FACTORY = 0
        
        def __init__(self, xname):
                
                Employee.ID_FACTORY += 1
                self.ID = Employee.ID_FACTORY
                self.name = xname
                terminated = False
        def __str__(self):
                return "{}({})".format(self.name, self.ID)

class FullTime(Employee):

        def __init__(self, xname, xsalary = 60000):
                Employee.__init__(self, xname)
                self.salary = xsalary
                self.interns = []

        def give_raise(self, amnt):
                self.salary += amnt

        def __add__(self, intern):
                self.interns.append(intern)
                intern.supervisor = self
        
        def fire(self):
                for intern in self.interns:
                        intern.supervisor = False
                self.terminated = True
        
        def showInterns(self):
                print("Interns:")
                for i in self.interns:
                        print(i.name)

class Intern(Employee):

        def __init__(self, xname, xwage = 10):
                Employee.__init__(self, xname)
                self.wage = xwage
                self.supervisor = False
                
        def give_raise(self, amnt):
                self.wage += amnt
        
        def __add__(self, supervisor):
                supervisor + self
        
        def fire(self):
                if self.supervisor:
                        self.supervisor.interns.remove(self)
                self.supervisor = False
                self.terminated = True
        def __str__(self):
                return Employee.__str__(self) + " Supervisor: {}".format(self.supervisor)


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

