import random

class Person(object):

    def __init__(self, Mom="ALPHA", Dad="ALPAH"):
        self.Mom = Mom
        self.Dad = Dad
        if not(Mom == "ALPHA" or Dad == "ALPHA"):
            self.eyes = random.choice([Mom.eyes, Dad.eyes])
            self.hair = random.choice([Mom.hair, Dad.hair])

    def __add__(self, mate):
        
        return Person(self, mate)

    def __str__(self):

        return "{} hair & {} eyes".format(self.hair, self.eyes)

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
