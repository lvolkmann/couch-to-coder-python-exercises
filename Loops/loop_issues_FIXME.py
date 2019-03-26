"""
What is the output of the following?
What if the check condition was == instead of !=?
"""

x=1
y=100

while x != y:
	print(x,y)
	x*=2
	y/=2
	

# Solution:
# 1) Runtime Error: Infinite Loop
# 2) The loop would never be entered.
