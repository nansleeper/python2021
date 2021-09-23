import turtle
import math

def star(n, radius):
    alpha = 180 - 180 * (n - 2) / n
    alpha_rad = alpha / 180 * math.pi
    a = radius * math.cos((math.pi - alpha_rad) / 2) / math.cos(alpha_rad)
    for k in range(n):
        turtle.forward(a)
        turtle.right(180 - 2 * alpha)
        turtle.forward(a)
        turtle.left(180 - alpha)

k = int(input())
star(int(input()), k)