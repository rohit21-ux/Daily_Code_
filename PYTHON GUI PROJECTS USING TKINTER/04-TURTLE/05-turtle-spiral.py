import turtle

t = turtle.Turtle()
t.speed(0)  # Fastest speed
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(100):
    t.color(colors[i % 6])
    t.forward(i)
    t.left(59)

turtle.done()
