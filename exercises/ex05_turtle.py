"""Exercise 5 - Turtle."""

__author__ = "730659395"

from turtle import Turtle, colormode, done
colormode(255)
t: Turtle = Turtle()

i: int = 0
t.penup()
t.goto(-100, -43)  #centering
t.color("blue")
colors = ["red", "blue", "green"]
t.pendown()
while i < 3:
    # t.color(colors[i])
    t.color(99, 204, 250)
    t.forward(200)
    t.left(120)
    i += 1
t.end_fill()
done()

# carolina blue: 99, 204, 250
