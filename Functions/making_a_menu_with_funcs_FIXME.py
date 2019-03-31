"""
Complete the program below by defining the following functions stubs
Perform function calls in the menu to use those definitions
* Try to define the functions so they take advantage of user data to add some personality
"""

import time
import random

menu = """
Howdy Campers. I'm a menu
What do you want from me?
1. Date
2. Time
3. Tell me a joke
4. Random Number Generator
5. Get away from me
"""

def get_choice(name):
	"""Gets valid input from user between 1 and 5"""


def get_date(name, age):
	"""Gets the date and predicts the mortality of the user"""


def get_time(name):
	"""Gets the time"""


def get_joke(name):
	"""Gets a hysterical joke"""


def get_random(name):
	"""Gets random number between one and 100000"""


run = True
user_name = input("Before we begin, what shall I call you?")
user_age = int(input("How long have you been alive?"))

while run:

	print(menu)
	choice = None # function call
	if choice == 1:
		pass # function call
	elif choice == 2:
		pass # function call
	elif choice == 3:
		pass # function call
	elif choice == 4:
		pass # function call
	elif choice == 5:
		run = False
		print("I didn't want to play with you anyway,", user_name)
