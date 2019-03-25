"""
Person Class:
String representation: "Hair Color  & Eye Color"
Person1 + Person2 = Person3
    Where Person 3 has a 50% chance of
    'inheriting' eye and hair color from either parent
Keeps Track of Parent Objects
"""

class Person(object):

    def __init__(self, Mom="ALPHA", Dad="ALPAH"):
        self.Mom = Mom
        self.Dad = Dad
        if not(Mom == "ALPHA" or Dad == "ALPHA"):
            #FIXME
            pass


p1 = Person()
p1.eyes = "blue"
p1.hair = "blonde"
p2 = Person()
p2.eyes = "brown"
p2.hair = "burnette"

c1 = p1 + p2
c2 = p1 + p2
c3 = c1 + c2

print("Parents:",p1, p2)
print("Children:", c1, c2)
print()

print("Parents:",c1, c2)
print("Children:", c3)
print()

print(c3.Mom == c1)
