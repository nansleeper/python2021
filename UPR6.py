import turtle
from random import randint
import math

num_of_turt = 10
time = 10000

a = []
i = 0

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)

turt_syst = [turtle.Turtle(shape = 'turtle') for i in range(num_of_turt)]
for unit in turt_syst:
    a.append([randint(-150,150), randint(-150, 150), randint(0, 360)])
    unit.penup()
    unit.speed(100)
    unit.goto(a[i][0], a[i][1])
    unit.left(a[i][2])
    
    i+=1

print(a)

for k in range(time):
    for unit in turt_syst:
        i = -1
        for unit in turt_syst:
            i += 1
            if a[i][0] + 2 * math.cos(a[i][2] / 180 * math.pi) <= - 199 or a[i][0] + 2 * math.cos(a[i][2] / 180 * math.pi) >= 199:
                print(a[i][2])
                a[i][2] = 540 - a[i][2]
            if a[i][1] + 2 * math.sin(a[i][2] / 180 * math.pi) >= 199 or a[i][1] + 2 * math.sin(a[i][2] / 180 * math.pi) <= -199:
                a[i][2] = 360 - a[i][2]
            a[i][0] += 2 * math.cos(a[i][2] / 180 * math.pi)
            a[i][1] += 2 * math.sin(a[i][2] / 180 * math.pi)
            unit.goto(a[i][0], a[i][1])
