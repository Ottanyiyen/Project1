from turtle import *

# Set up the window
setup(500, 500)
bgcolor('black')
right(90)

# Function to draw the rectangle part of the logo
def draw_rectangle(x, y):
    up()
    goto(x, y)
    down()
    fillcolor('red')
    begin_fill()
    for i in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()

# Function to draw the slanted part of the logo
def draw_slanted_part():
    up()
    goto(-40, 0)  # Adjust starting position for the slanted part
    down()
    left(22)
    begin_fill()
    for i in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()

# Draw the two rectangles
draw_rectangle(-100, 0)  # Adjusted to center the rectangles
draw_rectangle(0, 0)     # Adjusted to center the rectangles

# Draw the slanted part
draw_slanted_part()

# Hide the turtle and finish
hideturtle()
done()