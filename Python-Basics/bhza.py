import turtle
import time
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Happy Birthday Animation")

# Create turtle for text
text = turtle.Turtle()
text.hideturtle()
text.color("darkred")
text.penup()

# Draw balloons
def draw_balloon(color, x, y):
    balloon = turtle.Turtle()
    balloon.shape("circle")
    balloon.color(color)
    balloon.penup()
    balloon.goto(x, y)
    balloon.speed(0)

    # Balloon string
    string = turtle.Turtle()
    string.hideturtle()
    string.color("black")
    string.penup()
    string.goto(x, y - 15)
    string.pendown()
    string.goto(x, y - 50)

def show_text():
    text.goto(0, 0)
    text.write("🎂 Happy Birthday! 🎉", align="center", font=("Comic Sans MS", 24, "bold"))
    time.sleep(2)
    text.goto(0, -40)
    text.write("Wishing you joy and fun!", align="center", font=("Comic Sans MS", 18, "normal"))

# Show multiple balloons with animation
colors = ["red", "green", "yellow", "blue", "purple", "orange"]
for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-100, 150)
    draw_balloon(random.choice(colors), x, y)
    time.sleep(0.3)

# Show birthday message
show_text()

# Keep the screen open
turtle.done()
