from random import randint
import turtle

number_of_turtles = 5
steps_of_time_number = 100

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for a in pool:
    a.penup( )
    a.speed(50)
    a.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for a in pool:
        a.forward(2)