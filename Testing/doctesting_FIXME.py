"""
Create docstring tests for the following functions
"""
import doctest

# Example
def get_area_rect(length, width):
        """Returns area of rectangle
        >>> get_area_rect(5 , 5)
        25
        >>> get_area_rect(5 , 0)
        Traceback (most recent call last):
        ...
        ValueError
        >>> get_area_rect(5 , -1)
        Traceback (most recent call last):
        ...
        ValueError
        """
        
        if(length <=  0) or (width <= 0):
                raise ValueError
        return length * width

# Your turn
def validate_input(x):

        x = int(x)
        if 1 <= x <= 10:
                return True
        else:
                return False

def true_if_hello(x):

        x = str(x)
        if x == 'hello':
                return True
        return False

doctest.testmod()
