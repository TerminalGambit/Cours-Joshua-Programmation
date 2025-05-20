import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing

# Function to draw a filled hexagon
def draw_hexagon(side_length):
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.left(60)
    t.end_fill()

# Draw outer circle for the ball
t.penup()
t.goto(0, -150)  # Start at bottom of circle
t.pendown()
t.pensize(3)
t.color("black")
t.circle(150)

# Position turtle at center
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

# Settings for hexagons
hex_radius = 40  # Size of the hexagons
num_hexes = 6    # How many to place around

t.fillcolor("black")

# Draw center hexagon
draw_hexagon(hex_radius)

# Draw surrounding hexagons in a circular pattern
for angle in range(0, 360, 60):  # 6 directions
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(hex_radius * 2)  # Space out from center
    t.pendown()
    draw_hexagon(hex_radius)

# Hide turtle and display
t.hideturtle()
screen.mainloop()