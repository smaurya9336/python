from turtle import *
import turtle
t=Turtle()
s=Screen()
s.title("Sarita Maurya Graphics")
#s.bgcolor("yellow")
s.bgpic("")
t.shape("turtle")
t.color("black","green")
t.speed(1)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
penup()
t.forward(200)
pendown()
for i in range(4):
    t.forward(100)
    t.left(90)


t.end_fill()
hideturtle()
done()
