import turtle
import math

def round (radius):
    k = 40
    alpha = 180 - (k - 2) * 180 / k
    turtle.right(90 - alpha / 2)
    for i  in range(k):
        turtle.forward(2 * math.pi * radius / k)
        turtle.left(alpha)
    turtle.left(90 - alpha / 2)

radius = 20



for k in range(int(input())):
    round(radius)
    turtle.left(180)
    round(radius)
    radius+=20
    turtle.left(180)