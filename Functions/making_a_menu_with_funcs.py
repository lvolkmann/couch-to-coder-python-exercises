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
	while True:
		response = int(input())
		if 1 <= response <= 5:
			return response
		else:
			print("That's outside the scope of my intelligence... Try again,", name)

def get_date(name, age):
	"""Gets the date and predicts the mortality of the user"""
	print("It's currently", time.ctime(), name, ". You probably have,", (80 - age), "good years left.")

def get_time(name):
	"""Gets the time"""
	print(time.ctime())

def get_joke(name):
	"""Gets a hysterical joke"""
	print(name,"...enough said.")

def get_random(name):
	"""Gets random number between one and 100000"""
	print("I have assigned you a number,", name, ". That number is", random.randint(0,10000))

run = True

user_name = input("Before we begin, what shall I call you?")
user_age = int(input("How long have you been alive?"))

while run:
	print(menu)
	choice = get_choice(user_name)
	if choice == 1:
		get_date(user_name, user_age)
	elif choice == 2:
		get_time(user_name)
	elif choice == 3:
		get_joke(user_name)
	elif choice == 4:
		get_random(user_name)
	elif choice == 5:
		run = False
		print("I didn't want to play with you anyway,", user_name)
