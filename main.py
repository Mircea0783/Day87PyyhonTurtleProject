import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)  # 20px high, 100px wide
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 3  # Ball speed in x direction
ball.dy = -3  # Ball speed in y direction

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):  # 5 rows of bricks
    for x in range(-350, 400, 100):  # 8 bricks per row
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=4)  # 20px high, 80px wide
        brick.penup()
        brick.goto(x, 200 - y * 30)  # Position bricks
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -350:  # Left boundary
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 350:  # Right boundary
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()  # Manually update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.xcor() > 390:  # Right wall
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:  # Left wall
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:  # Top wall
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:  # Bottom (game over condition)
        ball.goto(0, -230)
        ball.dy *= -1  # Reset ball

    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250 and
        ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision
    for brick in bricks[:]:  # Iterate over a copy to allow removal
        if (ball.distance(brick) < 40):  # Rough collision detection
            ball.dy *= -1  # Bounce ball
            brick.goto(1000, 1000)  # Move brick off-screen
            bricks.remove(brick)  # Remove from list
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Win condition
    if len(bricks) == 0:
        ball.hideturtle()
        score_display.goto(0, 0)
        score_display.write("You Win!", align="center", font=("Courier", 36, "normal"))
        break

    time.sleep(0.01)  # Control game speed

screen.mainloop()  # Keep window open
