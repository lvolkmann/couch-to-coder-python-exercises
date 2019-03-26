"""
What is the output of the following code? Why?
"""

x = 7
status = True

if x < 10 and not status:
	print (1)
elif x < 2 or status:
	print (2)
elif x != 3 and status:
	print(3)
else:
	print(4)

