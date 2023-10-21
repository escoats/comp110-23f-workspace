"""Turtle functions"""

from turtle import Turtle, colormode, done

colormode(255)

t: Turtle = Turtle() # initialize turtle, named t

t.speed(5) # 1 to 10
t.hideturtle()

t.penup() # pen up
t.pendown() # pen down
t.goto(0, 0) # teleport to coords

t.fillcolor("pink") # sets fill color
t.begin_fill()
# code for shape to be filled
t.end_fill()

linecolor = "blue"
fillcolor = "pink"
t.color(linecolor, fillcolor)

t.begin_fill()
t.circle(50)
t.end_fill()

t.pencolor("green")

# carolina blue: 99, 204, 250
t.color(99, 204, 250)
done()