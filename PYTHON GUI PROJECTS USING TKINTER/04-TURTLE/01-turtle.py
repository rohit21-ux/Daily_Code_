import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Demo")

# Create turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(2)

# Draw something
pen.forward(100)
pen.left(90)
pen.forward(100)

# Exit on click
screen.exitonclick()
