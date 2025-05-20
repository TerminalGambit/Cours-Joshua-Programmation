import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.speed(1)  # Slow so the child can see what's happening

# Rectangle dimensions
length = 200
width = 100

# Draw the rectangle
for _ in range(2):  # Loop twice: length + width = 4 sides
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)

# Hide the turtle so it looks cleaner
t.hideturtle()

# Keep the window open
screen.mainloop()