import turtle
import math


n = float(input())

f = 300
for k in range(0, f, 1):
    turtle.goto(n * k / 10 * math.cos(k / 10), n * k / 10 * math.sin(k / 10))