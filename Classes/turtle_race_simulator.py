import random
import time
turtle_names = ["Lenny", "George", "Ken", "Dylan", "Ralph"]

def summon_turtles(turtle_names):
    turtles = []
    for turtle_name in turtle_names:
        turtles.append([0,turtle_name])
    return turtles

def turtle_walk(turtleLst):
    for turtle in turtleLst:
        turtle[0] += random.randint(1,10)

def show_standing(turtleLst):
    turtleLst.sort(reverse=True)
    for place in range(len(turtleLst)):
        print(place+1, "place:", turtleLst[place][1], "@" , turtleLst[place][0], "meters")

def race(turtleLst, distance):
    while True:
        turtle_walk(turtleLst)
        print()
        show_standing(turtleLst)
        time.sleep(2)
        
        for turtle in turtleLst:
            if turtle[0] > distance:
                return turtle[1]

turtleRacers = summon_turtles(turtle_names)
winner = race(turtleRacers, 100)

print()
print("Our winner is:", winner, "!")
