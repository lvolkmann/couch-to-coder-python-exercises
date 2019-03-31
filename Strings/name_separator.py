"""
Write a program to take the list of names below and print

"Hello, {first} {last}"

for each item in the list

"""

names = ["Jobs, Steve", "Gates, Bill", "Musk, Elon", "Hopper, Grace"]

#Create a for loop to get each full name
for full_name in names:
	#Method for finding the separator
	sep = full_name.find(",")
	#get first
	first = full_name[sep + 2:]
	#get last
	last = full_name[0:sep]
	#print results
	print("Hello", first, last)
