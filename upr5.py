import turtle

for k in range(0, 210, 20):
    for n in range(4):
        turtle.forward(20+k)
        turtle.right(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.backward(10)
    turtle.pendown()
