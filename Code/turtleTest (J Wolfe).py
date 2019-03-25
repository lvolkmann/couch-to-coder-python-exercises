import turtle
import random

runnerList = ['Steve', 'Bob', 'Jimbo']
runnerList = [[runner, turtle.Turtle()] for runner in runnerList]

screen = turtle.Screen()
screen.delay(0.1)
yPos = 150
xPos = 250
screen.screensize(xPos, yPos)
screen.colormode(255)

for runner in runnerList:
    runner[1].penup()
    color = (random.randint(1, 255),
             random.randint(1, 255),
             random.randint(1, 255))
    runner[1].color(color, color)
    runner[1].setpos(-xPos, yPos)
    yPos += 50
    runner[1].pendown()

screen.delay(50)
winner = False
while not winner:
    for runner in runnerList:
        runner[1].forward(random.randint(1, 50))
        if runner[1].pos()[0] >= xPos:
            winner = True
            print(runner[0] + ' wins!')
            break

print()

for runner in runnerList:
    print(runner[0] + ' ' + str(runner[1].pos()[0] + xPos))
