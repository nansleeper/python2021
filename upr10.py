import turtle
import math


def round ():
    k = 40
    alpha = 180 - (k - 2) * 180 / k
    turtle.right(90 - alpha / 2)
    for i  in range(k):
        turtle.forward(10)
        turtle.left(alpha)
    turtle.left(90 - alpha / 2)


for i in range(6):
    turtle.left(60)
    round()
    
