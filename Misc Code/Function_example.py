def my_func(n: int, out: str) -> int:
"""Pass in integer and string. 
Function will output the string n times.
Function returns n incremented by 1.
"""
	print(n*out)
	return n + 1

n = 1
ch = '*'

while(n <= 10):
	n = my_func(n, ch)

print("done")

for row in range(1,10):
	my_func(row, ch)

print("done")