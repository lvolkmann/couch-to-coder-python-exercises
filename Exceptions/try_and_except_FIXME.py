"""
Write a function divider() that gets two numbers from the user and return the division of the two
Implement try and except such that:
    - it handles zero division errors
    - it throws and handles an error if the divisor is 7 (and throws a specific error message)
    - it handles if a naughty user tries to divide by a string
    - it handles all other exceptions
"""

def divider():
    try:
        x = int(input("First Number"))
        y = int(input("Second Number"))

        if y == 7:
            raise TypeError("7 isn't even a real number")

        return x/y

    except ValueError:
        print("Must input a number")

    except ZeroDivisionError:
        print("Can't divide by zero")
        
    except TypeError as baddy:
        print (baddy)
    except:
        print("Something Went Wrong")
        
    
