import turtle

x = 0
y = 0
Vx = 10
Vy = 30
ay = -10
dt = 0
while 1 != 0:
    dt+= 0.0001
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2
    Vy += ay * dt
    turtle.goto(x, y)
    if y <= 0:
        Vy = (-0.8) * Vy