import random

class AlphaParent(object):

	def __init__(self, eye_color, hair_color):
		self.eyes = eye_color
		self.hair = hair_color
		
	def __add__(self, mate):
		return Child(self,mate)
	
	def __str__(self):
		return "{} hair - {} eyes".format(self.hair, self.eyes)

class Child(AlphaParent):

	def __init__(self, mom, dad):
		self.mom = mom
		self.dad = dad
		self.eyes = random.choice([mom.eyes, dad.eyes])
		self.hair = random.choice([mom.hair, dad.hair])
	
	def twenty_three_and_me(self, great = -1):
		pass

	def outputGeneration(self, mom, dad, great):
	
		if(great > 0):
			print("Great" * great, "GrandFather:", dad)
			print("Great" * great, "GrandMother:",  mom)
		if great == 0:
			print("GrandFather:", dad)
			print("GrandMother:",  mom)
		if great == -1:
			print("Father:", dad)
			print("Mother:", mom)

if __name__ == "__main__":
    
    a1 = AlphaParent("Blue", "Blonde")
    a2 = AlphaParent("Brown", "Burnette")
    a3 = AlphaParent("Blue", "Red")
    a4 = AlphaParent("Blue", "Burnette")

    b1 = a1 + a2
    b2 = a3 + a4

    c1 = b1 + b2


    c1.twenty_three_and_me()
    print()
    print(c1)





