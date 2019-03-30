def string_breakdown(the_string :str) -> list:
    """Accepts a string and returns a list of tuples of form [(char, count)]"""
    
    checked = []
    components = []   
    
    for char in the_string:
        
        if char not in checked:
            count = the_string.count(char)
            checked.append(char)
            components.append((char, count))

    return components

def print_breakdown(component_list_of_tuples:list):
    """Prints a list of tuples of form [(char, count)]"""
    
    for tup in component_list_of_tuples:
        print("{}:{}".format(tup[0], tup[1]))

#Test
string = "Hello, my name is Landon. What's yours? I bet it's Beth. You look like a Beth"
string_comp = string_breakdown(string)
string_comp.sort()

print_breakdown(string_comp)


letters = ["a", "b", "c", "d"]

for char in letters:
    print(char)

print()

i = 0
while i < len(letters):
    print(letters[i])
    i += 1
