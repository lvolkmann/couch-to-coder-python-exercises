"""
Predict the output of the problems below
with input 5 and 3.14 respectively
"""

# Problem 1:
age = input("Input your age: ")
dog_coefficient = 7
dog_years = age * dog_coefficient
print(dog_years, type(dog_years))

# Solution: "5555555" <class 'str'>
# Haha did I trick ya?

# Problem 2:
num_type_1 = float(input("What’s your favorite number?"))
num_type_2= int(num_type_1)
num_type_3 = str(num_type_2)
num_type_4=bool(num_type_3)

print(num_type_1, num_type_2, num_type_3, num_type_4)

# Solution: 3.14 3 "3" True