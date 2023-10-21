"""Exercise 5 - Turtle."""

__author__ = "730659395"

from turtle import Turtle, colormode, done
colormode(255)
t: Turtle = Turtle()

t.speed(10) # 1 to 10
t.hideturtle()

def teleport(x: int, y: int) -> None:
    """Teleports the turtle to the given coordinates."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def petals(scale: int, radius: int) -> None:
    """Draws two opposing flower petals."""
    length = 100 * scale
    t.forward(length)
    t.circle(radius, 180)
    t.forward(length*2)
    t.circle(radius, 180)
    t.forward(length)

def center(radius: int) -> None:
    """Draws the daisy's center."""
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(radius)
    t.end_fill()

def daisy(scale: int, radius: int, x: float, y: float, num_petals: int) -> None:
    """Draws a daisy."""
    t.penup()
    t.goto(x+radius, y)
    t.pendown()

    # loops through petals
    t.fillcolor("pink")
    t.begin_fill()
    for petal in range(0, num_petals):
        petals(scale, radius)
        t.circle(radius, 180/num_petals)
    t.end_fill()

    # draws and colors the daisy's center
    center(radius)

def pointy_petal():
    t.circle(200, 180/5)
    t.left(140)
    t.circle(200, 180/5)

def pointy_flower(num_petals):
    t.begin_fill()
    t.fillcolor("purple")
    for petal in range(0, num_petals):
        pointy_petal()
    t.end_fill()

    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(5)
    t.end_fill()

pointy_flower(12)
#daisy(0.5, 20, 15, 15, 10)
#daisy(1, 20, -100, -200, 4)
done()