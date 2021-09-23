import turtle
import math

def prav(n, radius):
    alpha = 180 - (((n - 2) * 180) / n)
    edge = radius * (2 - 2 * math.cos(alpha / 180 * math.pi)) ** 0.5 
    turtle.penup()
    turtle.forward(radius)
    turtle.left(90 +  alpha / 2)
    turtle.pendown()
    for i in range(n):
        turtle.forward(edge)
        turtle.left(alpha)
    turtle.left(90 - alpha / 2)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(180)

radius = 0

for n in range(3, 13):
    radius += 20
    prav(n, radius)