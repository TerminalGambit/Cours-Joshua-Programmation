import turtle

# Setup screen and add shape
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Interactive Football Pitch")

# Drawing turtle for static elements
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

# Function to draw a player
def draw_player(x, y, color):
    player = turtle.Turtle()
    player.shape("circle")
    player.color(color)
    player.penup()
    player.goto(x, y)
    player.stamp()
    player.hideturtle()

# Function to create the ball
def create_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("black")
    ball.penup()
    ball.goto(0, 0)
    return ball

# Display the logo as text
def setup_logo():
    t.penup()
    t.goto(-180, 80)
    t.pendown()
    t.write("Man City", font=("Arial", 16, "bold"))

# Movement functions for the ball
def move_up():
    y = ball.ycor()
    ball.sety(y + 10)

def move_down():
    y = ball.ycor()
    ball.sety(y - 10)

def move_left():
    x = ball.xcor()
    ball.setx(x - 10)

def move_right():
    x = ball.xcor()
    ball.setx(x + 10)

# Main function to run everything
def main():
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

    # Add players
    draw_player(-100, 0, "blue")   # Defender
    draw_player(100, 0, "red")     # Striker
    draw_player(0, 80, "green")    # Midfielder

    # Display logo
    setup_logo()

    # Create ball
    global ball
    ball = create_ball()

    # Keyboard bindings
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")

    # Hide drawing turtle
    t.hideturtle()

    # Keep the window open
    screen.mainloop()

# Run the main function
if __name__ == "__main__":
    main()