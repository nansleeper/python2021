import turtle

a = [(0, 0), (0, 30), (30, 0), (30, 30), (0, 60), (30, 60)]


s = open('upr2').read()

if s[-1] == '\n':
    s = s[:-1]

ch = s.split(', ')

turtle.penup()

turtle.speed(1)
def pechat(x, n):
    for k in list(ch[x]):
        if k == 's':
            turtle.pendown()
        else:
            print(k)
            turtle.goto(40 * n + a[int(k)][0], a[int(k)][1])
    turtle.penup()

pechat(int(input()), int(input()))
print(ch)