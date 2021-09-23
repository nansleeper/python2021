import turtle

k=int(input())
for n in range(k):
    turtle.forward(50)
    turtle.right(180-((k-2)/k)*180)