"""
Trace through the code for each of the problems below with every starting value
Predict the output
"""

# Problem 1:

# Try with:
num = 47.2
# num = 0
# num = 0.5
# num = -5

if num >= 1:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# solutions: Positive number, zero, negative number, negative number

# Problem 2:

    # Try with:
    grade = 45
	# grade = 75
	# grade = 105

    if grade >= 90:
        print("You received an A")

    if grade >= 80:
        print("You received a B")

    if grade >= 70:
        print("You received a C")

    if grade >= 60:
        print("You received a D")
    else:
        print("Sorry, you received an F")

    # solutions: F; C, D; A,B,C,D
    # Note that this code contains a logical error but is still completely valid
    # Getting good at tracing is being able to read the code for what it does, not what it should do