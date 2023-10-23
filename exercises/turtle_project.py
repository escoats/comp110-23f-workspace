"""Exercise 5 - Turtle. Draws a field of flowers!

7. Above and beyond - Daisy function (lines 36-58) is broken up further into functions called petals (lines 19-25) and center (lines 28-33).
8. Above and beyond - Circle function is called on lines 50, 52, and 139.
Setheading function is called on lines 122 and 139.
Width setting is changed on lines 134 and 152.
"""

__author__ = "730659395"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    # Initialize turtle and turtle settings.
    t: Turtle = Turtle()
    t.speed(0)
    t.hideturtle()
    colormode(255)

    # Draw flowers!
    pointy_flower(t, 200, 100, 12)
    pointy_flower(t, -150, -100, 10)
    daisy(t, -100, 200, 100, 10, 10)
    daisy(t, -250, 35, 10, 5, 4)
    daisy(t, 50, -60, 30, 15, 6)
    daisy(t, 175, -200, 75, 15, 15)
    
    sprout_coords: list[list[float]] = [[-250, 200], [-200, -300], [20, 20], [200, 250]]
    for spot in sprout_coords:
        sprout(t, spot[0], spot[1])
    
    shroom_coords: list[list[float]] = [[-25, 25], [-300, -200], [50, -150], [250, -70], [50, 325]]
    for spot in shroom_coords:
        mushroom(t, spot[0], spot[1])

    # Finish
    done()


def teleport(t: Turtle, x: float, y: float) -> None:
    """Teleports the turtle to the given coordinates."""
    t.penup()
    t.goto(x, y)
    t.pendown()


def petals(t: Turtle, petal_length: int, center_radius: int) -> None:
    """Draws two opposing daisy petals."""
    t.forward(petal_length)
    t.circle(center_radius, 180)
    t.forward(petal_length * 2)
    t.circle(center_radius, 180)
    t.forward(petal_length)


def center(t: Turtle, center_radius: int) -> None:
    """Draws the daisy's center."""
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(center_radius)
    t.end_fill()


def daisy(t: Turtle, x: float, y: float, petal_length: int, center_radius: int, num_petals: int) -> None:
    """Draws a daisy."""
    # sets color for flower
    t.pencolor("light sky blue")
    
    # Sends turtle to correct location
    t.penup()
    t.goto((x + center_radius), y)
    t.pendown()

    # Loops through petals
    t.fillcolor("pink")
    t.begin_fill()
    for petal in range(0, num_petals):
        petals(t, petal_length, center_radius)
        t.circle(center_radius, (180 / num_petals))
    t.end_fill()

    # Draws and colors the daisy's center
    center(t, center_radius)
    
    # Turns color back to default
    t.pencolor("black")


def pointy_petal(t: Turtle) -> None:
    """Draws an angled petal."""
    t.circle(200, 36)
    t.left(140)
    t.circle(200, 36)


def pointy_flower(t: Turtle, x: float, y: float, num_petals: int) -> None:
    """Uses the pointy_petal function to draw a flower with pointy petals."""
    teleport(t, x, y)
    
    # Draw petals
    t.pencolor("teal")
    t.begin_fill()
    t.fillcolor("purple")
    for petal in range(0, num_petals):
        pointy_petal(t)
    t.end_fill()
    
    # Draw center
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(5)
    t.end_fill()
    t.pencolor("black")


def sprout(t: Turtle, x: float, y: float) -> None:
    """Draws a sprout."""
    teleport(t, x, y)
    t.width(3)
    t.color("lime green")
    t.setheading(90)
    t.forward(15)
    t.circle(10, 90)
    teleport(t, x, (y + 15))
    t.setheading(90)
    t.circle(-10, 90)
    t.width(1)


def mushroom(t: Turtle, x: float, y: float) -> None:
    """Draws a mushroom."""
    t.width(5)
    t.color("orange red")
    teleport(t, x, y)

    # Head
    t.begin_fill()
    t.setheading(90)
    t.circle(10, 180)
    t.setheading(0)
    t.forward(20)
    t.end_fill()

    # Stem
    t.setx(x - 10)
    t.color("tan")
    teleport(t, (x - 10), (y - 2))
    t.setheading(270)
    t.forward(15)
    t.width(1)


if __name__ == "__main__":
    main()