"""
Create a dictionary from the list below using the enumerate() function
"""
l1 = ["a", "b", "c"]
some_dict = {}

for i, value in enumerate(l1):
    some_dict[i] = value

    
print(some_dict)
