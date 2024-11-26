from turtle import *  # Importing all functionalities of the turtle module

# Function to draw Logo 1
def draw_logo_1():
    bgcolor('red')  # Set the background color of the canvas to red
    right(90)  # Rotate the turtle 90 degrees to the right
    pencolor('black')  # Set the pen color to black
    hideturtle()  # Hide the turtle cursor for cleaner graphics

    # List of positions where the two rectangles will be drawn
    pos = [(-40, 0), (40, 0)]  
    
    # Loop to draw two vertical black rectangles
    for x, y in pos:
        up()  # Lift the pen up so it doesn't draw while moving
        goto(x, y)  # Move the turtle to the specified position
        down()  # Put the pen down to start drawing
        fillcolor('black')  # Set the fill color to black
        begin_fill()  # Start filling the shape with the fill color
        for _ in range(2):  # Loop twice to draw the rectangle
            forward(200)  # Move the turtle forward 200 units
            left(90)  # Turn the turtle left 90 degrees
            forward(40)  # Move the turtle forward 40 units
            left(90)  # Turn the turtle left 90 degrees
        end_fill()  # Complete the filling of the rectangle

    # Move the turtle to the starting position of the diagonal design
    up()  # Lift the pen up
    goto(-40, 0)  # Move the turtle to (-40, 0)
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
    bgcolor('black')
    right(90)
    pencolor('red')
    hideturtle()

    pos = [(-40,0), (40,0)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('red')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-40,0)
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
    bgcolor('yellow')
    right(90)
    pencolor('orange')
    hideturtle()

    pos = [(-40,0), (40,0)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('orange')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-40,0)
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
    bgcolor('#146385')
    right(90)
    pencolor('#311b07')
    hideturtle()

    pos = [(-40,0), (40,0)]
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
    goto(-40,0)
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
    bgcolor('#e27712')
    right(90)
    pencolor('#cdbaa8')
    hideturtle()

    pos = [(-40,0), (40,0)]
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
    goto(-40,0)
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
    bgcolor('#db1fa9')
    right(90)
    pencolor('#1d6e12')
    hideturtle()

    pos = [(-40,0), (40,0)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#1d6e12')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-40,0)
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
    bgcolor('#c81921')
    right(90)
    pencolor('#829857')
    hideturtle()

    pos = [(-40,0), (40,0)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#829857')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-40,0)
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
    bgcolor('#6d5d4f')
    right(90)
    pencolor('#1c2931')
    hideturtle()

    pos = [(-40,0), (40,0)]
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
    goto(-40,0)
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
    bgcolor('#1e8acc')
    right(90)
    pencolor('#085c5e')
    hideturtle()

    pos = [(-40,0), (40,0)]
    for x,y in pos:
        up()
        goto(x,y)
        down()
        fillcolor('#085c5e')
        begin_fill()
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
        end_fill()
    up()
    goto(-40,0)
    down()
    left(22)

    begin_fill()
    for _ in range(2):
        forward(217)
        left(68)
        forward(40)
        left(112)
    end_fill()