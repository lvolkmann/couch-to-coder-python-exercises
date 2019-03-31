"""Write code to satisfy the following comments"""

# create a while loop that counts from 1 to 20 that prints multiples of 3

count = 1
while count <=20:
	if(count % 3 == 0):
		print(count)
	count += 1

# create a for loop that counts from 1 to 20 that prints multiples of 3

for num in range(0,20,3):
	print(num)

# define and implement a function that takes 2 sides of a rectangle, prints the perimeter, and returns the area

def perimeter_and_area(s1, s2):
    """prints the perimeter and returns the area"""
    print(2*(s1+s2))
    return (s1*s2)

# define a function that takes two strings and checks to see if they're equal; if yes, return true and one of the strings; if no, concatenate and return false and result

def str_func(s1, s2):
	if s1 == s2:
		return True,  s1
	else:
		return False, (s1+s2)

# define a function that takes in a string and a character and returns a list of all the indexes of the occurrences of that character

def index_func(string, char):
    lst = []
    i = 0
    while True:
        new_i = string.find(char, i)
        if new_i == -1:
            return lst
        else:
            lst.append(new_i)
            i = new_i + 1
