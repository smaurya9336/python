import turtle
turtle.bgcolor("green")
draw = turtle.Turtle()
draw.speed(1000000)
draw.hideturtle()
draw.pensize(3)
draw.color("white")

def Board (a, x, y, size):
    draw.pu()
    draw.goto(x, y)
    draw.pd()
    for i in range (0, 4):
        draw.forward(size)
        draw.right(90)

x =-40
y = -40
size = 40
for i in range (0, 10):
    for j in range (0, 10):
         Board (draw, x + j*size, y + i*size, size)

turtle.done()

import tkinter
import tkinter.messagebox
window = tkinter.Tk()
def Button_click ():
   tkinter.messagebox.showinfo("Game", "Tic Tac Toe")

button = tkinter.Button(window, text = "Play!", command = Button_click)
button.pack()
window.mainloop()
