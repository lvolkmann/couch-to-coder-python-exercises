# Write a recursive function to model the formula below

# a0 = 1
# an = 5(an-1) + 7

def func(n):
    if(n==0):
        return 1
    else:
        return 5*(func(n-1)) + 7

# Write a recursive factorial function

def fact(n):
    if(n <= 1):
        return 1
    else:
        return n * fact(n-1)