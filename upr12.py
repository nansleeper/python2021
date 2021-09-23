import turtle
import math

def half (radius):
    k = 40
    alpha = 180 - (2 * k - 2) * 90 / k
    for i  in range(k):
        turtle.forward( math.pi * radius / k)
        turtle.left(alpha)

for k in range(int(input())):
    half(10)
    half(3)
