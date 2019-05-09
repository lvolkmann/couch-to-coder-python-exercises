class me:

    def __init__(self, xname, xage, jobx = "Student", wagex = 8):

        self.name = xname
        self.age = xage
        self.job = jobx
        self.wage = wagex

    def printMe(self):

        print("{} : {} : {}".format(self.name, self.age, self.job))

    def calcPay(self, hoursWorked):

        return self.wage * hoursWorked

test = me("Landon", 20)
test2 = me("Landon", 20, "SI")

test.printMe()
test2.printMe()

test3 = me("Landon", 20, "SI", 10)
print(test3.calcPay(8))

    
