"""
Define the functions below to get this turtle race simulator working
"""

import random
import time
turtle_names = ["Lenny", "George", "Ken", "Dylan", "Ralph"]

def summon_turtles(turtle_names):
    """Returns list of turtles[[distance = 0, name], [distance = 0, name]...] based on list of names passed"""
    turtles = []
    for turtle_name in turtle_names:
        turtles.append([0,turtle_name])
    return turtles

def turtle_walk(turtleLst):
    """Randomly increases every turtle position"""
    for turtle in turtleLst:
        turtle[0] += random.randint(1,10)

def show_standing(turtleLst):
    """Output turtle positions and their places in the race"""

    turtleLst.sort(reverse=True)
    for place in range(len(turtleLst)):
        print(place+1, "place:", turtleLst[place][1], "@" , turtleLst[place][0], "meters")

def race(turtleLst, distance):
    """Main loop"""
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
