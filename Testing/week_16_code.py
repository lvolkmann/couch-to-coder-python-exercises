#Week 16 Session 1

def get_area_rect(length, width):
        """Returns area of rectangle"""
        
        if(length <=  0) or (width <= 0):
                raise ValueError
        return length * width


def validate_input(x):
        """Validates that input give is between 1 and 10"""
        x = int(x)
        if 1 <= x <= 10:
                return True
        else:
                return False

def true_if_hello(x):
        """Will return true if and only if passed the str 'hello'"""

        x = str(x)
        if x == 'hello':
                return True
        return False
