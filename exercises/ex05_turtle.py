"""Exercise 5 - Turtle."""

__author__ = "730659395"

from turtle import Turtle, colormode, done
t: Turtle = Turtle()

i: int = 0
while i < 3:
    t.forward(100)
    t.left(120)
    i += 1

t.penup
t.goto(45, 45)
done()