#imports
import math

#define functions

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

#probably more functions, but the same basic format

#define variables outside loop

run = True
aff_input = ["YEAH", "YES", "YEP", "Y"]
function_calls = 0

#main loop
while run:
	upper_lim = int(input("What would you like the upper limit of the tested data set to be?"))
	
	for value in range(1,upper_lim):
		#implement functions
		print("Shape: Circle", "Circumference:", get_C_of_circle(value), "Area:", get_A_of_circle(value))
		print()
		
		function_calls += 2
	
	if input("Run again?\n").upper() in aff_input:
		run = True
	else:
		run = False
		print("Have a nice day")
