"""
Write a class that contains variables name, age, job, and wage
Write an init such that job defaults to student and wage defaults to 8
Define a printMe method to output variables "name : age : job"
Define a calcPay method that accepts integer float hoursWorked and returns pay
""" 

class me:
    pass

test = me("Landon", 20)
test2 = me("Landon", 20, "SI")

test.printMe()
test2.printMe()

test3 = me("Landon", 20, "SI", 10)
print(test3.calcPay(8))

    
