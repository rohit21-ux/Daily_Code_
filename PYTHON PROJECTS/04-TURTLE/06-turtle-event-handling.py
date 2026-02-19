import turtle

def move(x, y):
    t.goto(x, y)

t = turtle.Turtle()
screen = turtle.Screen()

screen.onscreenclick(move)
screen.mainloop()
