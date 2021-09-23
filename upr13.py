import turtle
import math

def round (radius, color):
    k = 40
    alpha = 180 - (k - 2) * 180 / k
    turtle.penup()
    turtle.forward(radius)
    turtle.right(270 - alpha / 2)
    turtle.begin_fill()
    for i  in range(k):
        turtle.pendown()
        turtle.forward(2 * math.pi * radius / k)
        turtle.left(alpha)
    turtle.color(color)
    turtle.end_fill()
    turtle.left(90 - alpha / 2)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(180)
    turtle.color("black")

def half (radius, color):
    k = 40
    turtle.color(color)
    alpha = 180 - (2 * k - 2) * 90 / k
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius)
    turtle.right(-90 - alpha / 2)
    for i  in range(k):
        turtle.pendown()
        turtle.forward(math.pi * radius / k)
        turtle.left(alpha)
    turtle.penup()
    turtle.left(90 - alpha / 2)
    turtle.forward(radius)
    turtle.color("black")

turtle.left(90)
turtle.forward(50)
round(100, "yellow")
turtle.left(30)
turtle.forward(50)
round(15, "blue") 
turtle.right(120)
turtle.forward(50)
round(15, "blue")
turtle.right(120)
turtle.forward(50)
turtle.left(30)
turtle.pendown()
turtle.width(5)
turtle.forward(30)
turtle.penup()
turtle.forward(20)
half(30, "red")


