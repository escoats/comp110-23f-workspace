"""follow along with turtle introduction"""


from turtle import Turtle, colormode, done
colormode(255)
t: Turtle = Turtle()
t2: Turtle = Turtle()

t.speed(5) # 1 to 10
t.hideturtle()

t.penup()
t.goto(-150, -75)
t.pendown()

t.pencolor("black")
t.fillcolor("black")

side_length: int = 300
t.begin_fill()
i: int = 0
while i < 3:
    t.forward(side_length)
    t.left(120)
    i += 1
t.end_fill()

t2.hideturtle()
t2.penup()
t2.goto(-150, -75)
t2.pendown()
t2.speed(10)
t2.color(99, 204, 250)
i2: int = 0
while i2 < 3:
    t2.forward(side_length)
    t2.left(120)
    i2 += 1

i2: int = 0
i3: int = 0
while i3 < 30:
    i2 = 0
    while i2 < 3:
        side_length *= 0.95
        t2.forward(side_length)
        t2.left(121)
        i2 += 1
    i3 += 1

done()