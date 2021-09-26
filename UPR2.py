import turtle

a = [(0, 0), (0, 30), (30, 0), (30, 30), (0, 60), (30, 60)]

ch = ['s04520', '1s52', '4s5302', '0s3154', '4s1352', '0s23145', '5s10231', '5s10231', '0s154', '0s452013', '0s35413']

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