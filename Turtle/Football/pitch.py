import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Function to draw a rectangle (used for pitch, penalty box, etc.)
def draw_rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Draw pitch outline
t.penup()
t.goto(-200, -100)
t.pendown()
draw_rectangle(400, 200)

# Center line
t.penup()
t.goto(0, -100)
t.setheading(90)
t.pendown()
t.forward(200)

# Center circle
t.penup()
t.goto(0, 0)
t.setheading(0)
t.forward(30)
t.left(90)
t.pendown()
t.circle(30)

# Left penalty area
t.penup()
t.goto(-200, -50)
t.setheading(0)
t.pendown()
draw_rectangle(50, 100)

# Right penalty area
t.penup()
t.goto(150, -50)
t.pendown()
draw_rectangle(50, 100)

# Left goal
t.penup()
t.goto(-210, -20)
t.setheading(0)
t.pendown()
draw_rectangle(10, 40)

# Right goal
t.penup()
t.goto(200, -20)
t.pendown()
draw_rectangle(10, 40)

# Hide turtle and finish
t.hideturtle()
screen.mainloop()