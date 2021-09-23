import turtle

n = int(input())
for k in range(n):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.right(360/n)