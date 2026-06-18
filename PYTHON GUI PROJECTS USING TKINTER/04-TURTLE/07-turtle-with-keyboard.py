import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    t.forward(50)

def turn_left():
    t.left(45)

def turn_right():
    t.right(45)

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.mainloop()
