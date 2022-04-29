import turtle
import math
import time

# Prompt the user for inputting two points
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

# Bresenham Line Draw Algorithm
dx = x2-x1
dy = y2-y1

x = x1
y = y1

e = 2 * dy-dx

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write('Point 1')

i = 1
while(i <= dx):
    time.sleep(1)
    turtle.goto(x, y)

    while(e >= 0):
        y = y + 1
        e += 2 * dx
    
    x = x + 1
    e = e + 2 * dy
    i = i + 1

turtle.goto(x2, y2) # Draw a line to (x2, y2)
turtle.write('Point 2')

turtle.penup()
turtle.hideturtle()
turtle.done()
