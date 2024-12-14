from turtle import *  # Importing all functionalities of the turtle module

# Function to draw Logo 1
def draw_logo_1():
    hideturtle()  # Hide the turtle cursor for cleaner graphics
    bgcolor('black')  # Set the background color of the canvas to red
    right(90)  # Rotate the turtle 90 degrees to the right
    pencolor('red')  # Set the pen color to black


    # List of positions where the two rectangles will be drawn
    pos = [(-60, 90), (22, 90)]
    # Loop to draw two vertical black rectangles
    for x, y in pos:
        up()  # Lift the pen up so it doesn't draw while moving
        goto(x, y)  # Move the turtle to the specified position
        down()  # Put the pen down to start drawing
        fillcolor('red')  # Set the fill color to black
        begin_fill()  # Start filling the shape with the fill color
        for _ in range(2):  # Loop twice to draw the rectangle
            forward(200)  # Move the turtle forward 200 units
            left(90)  # Turn the turtle left 90 degrees
            forward(40)  # Move the turtle forward 40 units
            left(90)  # Turn the turtle left 90 degrees
        end_fill()  # Complete the filling of the rectangle

    # Move the turtle to the starting position of the diagonal design
    up()  # Lift the pen up
    goto(-60, 90)  # Move the turtle to (-60, 90)
    down()  # Put the pen down to start drawing
    left(22)  # Turn the turtle left by 22 degrees to set the angle

    # Draw the diagonal trapezoid shape
    begin_fill()  # Start filling the shape with the fill color
    for _ in range(2):  # Loop twice to complete the shape
        forward(217)  # Move forward 217 units
        left(68)  # Turn the turtle left 68 degrees
        forward(40)  # Move forward 40 units
        left(112)  # Turn the turtle left 112 degrees
    end_fill()  # Complete the filling of the trapezoid

# Functionality of other logos (2-10) is similar; only the colors and parameters differ.
# The above explanation applies to other logos as well, with differences in `bgcolor`, `pencolor`, and `fillcolor`.

# To summarize:
# - `bgcolor`: Sets the background color of the canvas
# - `pencolor`: Sets the pen's drawing color
# - `fillcolor`: Sets the color used to fill shapes
# - `up()`: Lifts the pen so the turtle can move without drawing
# - `down()`: Puts the pen down to start drawing
# - `goto(x, y)`: Moves the turtle to a specific position
# - `right(angle)`: Rotates the turtle to the right
# - `left(angle)`: Rotates the turtle to the left
# - `forward(distance)`: Moves the turtle forward by a specified distance
# - `begin_fill()` and `end_fill()`: Starts and stops the filling of shapes
# - `hideturtle()`: Hides the turtle cursor


def draw_logo_2():
    hideturtle()
    bgcolor('black')
    right(90)
    pencolor('white')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('white')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_3():
    hideturtle()
    bgcolor('yellow')
    right(90)
    pencolor('#F52549')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('#F52549')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_4():
    hideturtle()
    bgcolor('#146385')
    right(90)
    pencolor('#311b07')


    pos = [(-60, 90), (22, 90)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#311b07')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60,90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_5():
    hideturtle()
    bgcolor('#e27712')
    right(90)
    pencolor('#cdbaa8')

    pos = [(-60, 90), (22, 90)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#cdbaa8')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60,90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_6():
    hideturtle()
    bgcolor('#46211A')
    right(90)
    pencolor('#F1D3B2')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('#F1D3B2')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_7():
    hideturtle()
    bgcolor('#375E97')
    right(90)
    pencolor('#FB6542')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('#FB6542')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_8():
    hideturtle()
    bgcolor('#66A5AD')
    right(90)
    pencolor('#C4DFE6')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('#C4DFE6')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_9():
    hideturtle()
    bgcolor('#6d5d4f')
    right(90)
    pencolor('#1c2931')

    pos = [(-60, 90), (22, 90)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#1c2931')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60,90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()


def draw_logo_10():
    hideturtle()
    bgcolor('#6AB187')
    right(90)
    pencolor('#20948B')

    pos = [(-60, 90), (22, 90)]
    for x, y in pos:
        up()
        goto(x, y)
        down()
        fillcolor('#20948B')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-60, 90)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()