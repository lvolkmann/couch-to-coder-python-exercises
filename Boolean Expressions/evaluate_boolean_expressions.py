"""
Predict the output of each of the boolean expressions below
"""

"Dog" and (5 > 2)
# True
(6 > 2) or ((582 % 17) != 9)
# True
"DOG" == "DOG" and 'cat'
# True
(5 + 2 * 3) == ((5+2) * 3)
# False
not(True or False)
# False
(21 % 2) == (97 % 2)
# True
bool((25 / 5) - 5)
# False
(((2 ** 19) % 2) > 0)
# False
(((18 * 23) ** 3) > 100000 ) or (((18 * 23) ** 3) <= 100000 )
# True