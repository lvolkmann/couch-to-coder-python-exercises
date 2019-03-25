"""
Get input for the following scenarios. Make sure the data is manipulatable.
1.	The name of the user
2.	How many children to they have?
3.	How old is there oldest child, if N/A input 0
4.	Are they married?
5.	What is their hourly wage?
"""

name = input("What is your name?")
children = int(input("How many children do you have?"))
eldest_child = int(input("If applicable, how old is your oldest child; else, enter 0"))
married = bool(input("If married enter 1, else enter 0"))
wage = float(input("What is your hourly wage?"))
