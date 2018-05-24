import turtle
import time
import random

colormode = 255
window = turtle.Screen()
window.bgcolor("purple")

tupac = turtle.Turtle()
number = 1
tupac.width(2)

arg = 1
var = 2
while number >= 0:

    window.colormode(255)
    tupac.pencolor((random.randrange(int(arg), int(var)), random.randrange(int(arg), int(var)), random.randrange(int(arg), int(var))))

    if var < 255:
        var += 1

    tupac.speed(0)
    tupac.left(90)
    tupac.circle(-20, 110)
    tupac.left(110)
    tupac.forward(55)
    tupac.circle(-12.5, 180)
    tupac.forward(5)
    tupac.right(90)
    tupac.forward(25)
    tupac.right(90)
    tupac.forward(5)
    tupac.circle(-12.5, 90)
    tupac.right(90)
    tupac.forward(7.5)
    tupac.backward(7.5)
    tupac.left(90)
    tupac.circle(-12.5, 90)
    tupac.forward(55)
    tupac.left(110)
    tupac.circle(-20, 110)
    tupac.left(120)
    if number % 12 == 0:
        tupac.left(5)

    number += 1
time.sleep(5)
