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
        """Validates that input give is between 1 and 10
        >>> validate_input(5)
        True
        >>> validate_input(-2)
        False
        >>> validate_input(12)
        False
        """
        x = int(x)
        if 1 <= x <= 10:
                return True
        else:
                return False

def true_if_hello(x):
        """Will return true if and only if passed the str 'hello'
        >>> true_if_hello('hello')
        True
        >>> true_if_hello('olleh')
        False
        >>> true_if_hello(7)
        False
        """

        x = str(x)
        if x == 'hello':
                return True
        return False

doctest.testmod()
