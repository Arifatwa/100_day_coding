# belajar turtle

import turtle
t=turtle.Turtle()

t.speed(50)
turtle.bgcolor("black")

for i in range(240):
    t.color("cyan")
    t.circle(i)
    t.left(5)

turtle.done()