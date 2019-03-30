import doctest

def calcVolume(l,w, h):
    """
>>> calcVolume(2,2,2)
8
>>> calcVolume(2, 2, -1)
Traceback (most recent call last):
...
ValueError
"""
    args = [l,w,h]
    for arg in args:
        int(arg)
        if arg <=0:
            raise ValueError
    return l * w * h

doctest.testmod()
