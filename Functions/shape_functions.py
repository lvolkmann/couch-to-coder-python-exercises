"""
Write a program to calculate the circumference and area of a circle
Get input from the user defining the range of the values to calculate circumference and area for

Within function definitions:
	Validate the input
	Output the data for each int in that range in the following form


Shape: {}, Circumference: {} Area: {}
Shape: {}, Circumference: {} Area: {}


Output the number of function calls
Ask the user if they’d like to run the program again
"""

# imports
import math

# define functions
def get_C_of_circle(radius :int) ->int:
	if radius <=0:
		print("Value must be greater than 0")
		return
	else:
		return 2* radius *math.pi
		
def get_A_of_circle(radius :int) ->int:

	if radius <=0:
		print("Value must be greater than 0")
		return
	else:
		return math.pi * (radius ** 2)


# define variables outside loop

run = True
aff_input = ["YEAH", "YES", "YEP", "Y"]
function_calls = 0

# main loop
while run:

	upper_lim = int(input("What would you like the upper limit of the tested data set to be?"))
	
	for value in range(1,upper_lim):

		# implement functions
		print("Shape: Circle", "Circumference:", get_C_of_circle(value), "Area:", get_A_of_circle(value))
		print()
		
		function_calls += 2
	
	print(function_calls)
	if input("Run again?\n").upper() in aff_input:
		run = True
	else:
		run = False
		print("Have a nice day")
