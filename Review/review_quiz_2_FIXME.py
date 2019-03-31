"""Answer the following questions"""

# 1
# What is the difference between a break and a continue statement?

# 2
# What is the result of the following?
for num in "blackjack-21":
	if (num.isdigit()):
		print(num)

# 3
# What is the result of the following?
def add_func(x : int, y : int) -> int:
	"""docstring goodness"""
	return  x + y

print(add_func(5,4))
print(add_func("cat", "dog"))
print(add_func("dog", 7))

# 4
# What is the result of the following?
print('5'.isalpha())
print('5'.isupper())
print('5'.isdigit())

# 5
# What is the result of the following code?
for num in range(0, 25, 6):
	if num % 12 == 0:
		print(num)

# 6
# What is always the value of the first index for any given, indexable data type?

# 7
# Define a function that returns true if the integer passed is less than 10 and greater than or equal to 1 and returns false in all other cases.

# 8
# What is the result of the following?
x = "9035768"
x[::-1]