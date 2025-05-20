import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(3)

# Helper function to draw the letter J
def draw_J():
    pen.setheading(0)
    pen.forward(20)
    pen.backward(10)
    pen.right(90)
    pen.forward(40)
    pen.circle(-10, 180)  # curve to the left
    pen.penup()
    pen.setheading(0)
    pen.forward(50)  # increased spacing to separate J and O
    pen.pendown()

def draw_O():
    pen.setheading(0)
    pen.circle(20)
    pen.penup()
    pen.forward(40)
    pen.pendown()

def draw_S():
    pen.setheading(0)
    pen.forward(20)
    pen.circle(10, 180)
    pen.forward(10)
    pen.circle(-10, 180)
    pen.forward(20)
    pen.penup()
    pen.setheading(0)
    pen.forward(40)
    pen.pendown()

def draw_H():
    pen.setheading(90)
    pen.forward(40)
    pen.backward(20)
    pen.right(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(20)
    pen.backward(40)
    pen.left(90)
    pen.penup()
    pen.forward(40)
    pen.pendown()

def draw_name():
    pen.penup()
    pen.goto(-200, 0)
    pen.setheading(0)
    pen.pendown()
    draw_J()
    draw_O()
    draw_S()
    draw_H()
    pen.hideturtle()

draw_name()
screen.mainloop()