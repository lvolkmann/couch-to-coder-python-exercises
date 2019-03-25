import random
import time

class Turtle:
	
	def __init__(self, xname):
		self.name = xname
		self.pos = 0
	
	def walk(self, hi):
		self.pos += random.randint(1,hi)
	
	def __str__(self):
		
		return "{} : {}".format(self.name, self.pos)
	
	def __eq__(self, turtle2):
	
		return self.pos == turtle2.pos
	
	def __nonzero__(self):
	
		return True

class Race:

	def __init__(self, name_lst, distance):
		self.turtles = self.summon_turtles(name_lst)
		self.winner = False
		self.upperWalkLimit = 10
		self.track = distance
	
	def summon_turtles(self, name_lst):
		turtles = []
		for name in name_lst:
			turtles.append(Turtle(name))
		return turtles
	
	def turtle_sort(self):
		self.turtles.sort(key=lambda turtle: turtle.pos, reverse = True)
	
	def display(self):
		self.turtle_sort()
		for turtle in self.turtles:
			print(turtle)
	
	def turtle_walk(self):
		for turtle in self.turtles:
			turtle.walk(self.upperWalkLimit)
	
	def check_win(self):
		self.turtle_sort()
		if self.turtles[0].pos >= self.track:
			self.winner = self.turtles[0]
	
	def display_neck_and_neck(self):
		for i in range(0,len(self.turtles)-1):
			if self.turtles[i] == self.turtles[i+1]:
				print(self.turtles[i].name, "and", self.turtles[i+1].name, "are neck and neck!")
				break
	
	def run_simulation(self):
		while not self.winner:
			self.display()
			time.sleep(2)
			self.display_neck_and_neck()
			self.turtle_walk()
			time.sleep(1)
			self.check_win()
			print()
		print("Our winner is:", self.winner)

turtle_names = ["Lenny", "George", "Ken", "Dylan", "Ralph"]

test = Race(turtle_names, 50)
test.run_simulation()
