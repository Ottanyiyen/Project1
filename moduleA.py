import turtle  # Import the turtle module for graphics
import random # Import the random module for generating random position of shapes


screen = turtle.Screen() # Create the screen object
screen.setup(width=800, height=600) # Set the screen dimensions

shadow_color = "gray"  # Define a consistent shadow color for the logo

def draw_frame():
    frame_pen = turtle.Turtle()  # Create a turtle for the main frame
    frame_pen.hideturtle()  # Hide the turtle cursor
    frame_pen.speed(0)  # Maximize drawing speed
    frame_pen.color("black")  # Set the pen color to black
    frame_pen.pensize(5)  # Increase the pen size for a bold frame


    shadow_pen = turtle.Turtle()  # Create a second turtle for the shadow frame
    shadow_pen.hideturtle()
    shadow_pen.speed(0)
    shadow_pen.color(shadow_color)
    shadow_pen.pensize(5)

    shadow_pen.penup()
    shadow_pen.goto(-400, 300)  # Start the shadow at the top-left corner
    shadow_pen.pendown()

    for _ in range(2):  # Loop twice for the rectangle (two long sides and two short sides)
        shadow_pen.forward(800)  # Draw the top and bottom edges
        shadow_pen.right(90)  # Turn 90 degrees to draw the next edge
        shadow_pen.forward(600)  # Draw the left and right edges
        shadow_pen.right(90)


    frame_pen.penup()
    frame_pen.goto(-400, 300)
    frame_pen.pendown()
    for _ in range(2):
        frame_pen.forward(800)
        frame_pen.right(100)  # This appears to be an error; the frame won't be rectangular.
        frame_pen.forward(600)
        frame_pen.right(100)


def add_background_decorations(color, shape, size):
    pen = turtle.Turtle()  # Create a turtle for background shapes
    pen.hideturtle()  # Hide the cursor
    pen.speed(0)  # Maximize drawing speed
    pen.color(color)  # Set the shape color


    for _ in range(15):  # Draw 15 random decorations
        pen.penup()
        pen.goto(random.randint(-300, 300), random.randint(-250, 250))  # Random positions
        pen.pendown()


        if shape == "circle":  # If the shape is a circle
            pen.begin_fill()
            pen.circle(size)  # Draw a filled circle
            pen.end_fill()

        elif shape == "square":  # If the shape is a square
            pen.begin_fill()
            for _ in range(4):
                pen.forward(size)  # Draw a side
                pen.right(90)  # Turn to create the next side
            pen.end_fill()

        elif shape == "star":  # If the shape is a star
            pen.begin_fill()
            for _ in range(5):
                pen.forward(size)
                pen.right(144)  # Angle for a 5-pointed star
            pen.end_fill()


def draw_logo(letter, color, bg_color, shape, size):
    screen.bgcolor(bg_color)  # Set the background color
    add_background_decorations(color, shape, size)  # Add decorative shapes
    draw_frame()  # Draw the frame


    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(5)

    pen.color(shadow_color)  # Set pen color to shadow color
    pen.penup()
    pen.goto(5, -5)  # Offset for shadow
    for _ in range(4):  # Shadow effect with multiple overdraws
        pen.write(letter, align="center", font=("Georgia", 150, "bold"))
        pen.penup()
        pen.goto(pen.xcor() + 2, pen.ycor() + 2)  # Move slightly for each shadow layer
        pen.pendown()


    pen.color(color)  # Switch to the main color
    pen.penup()
    pen.goto(0, 0)  # Center the main letter
    pen.pendown()
    for _ in range(4):  # Draw the main letter with a similar offset effect
        pen.write(letter, align="center", font=("Georgia", 150, "bold"))
        pen.penup()
        pen.goto(pen.xcor() + 2, pen.ycor() + 2)
        pen.pendown()


def draw_logo_1():
    draw_logo("A", "red", "#FFD700", "circle", 30)
# Similar functions for logos 2–10 with variations in parameters (color, background, shapes, sizes).


def draw_logo_2():
    draw_logo("A", "blue", "#8A2BE2", "square", 40)

def draw_logo_3():
    draw_logo("A", "green", "#FF4500", "star", 35)

def draw_logo_4():
    draw_logo("A", "yellow", "#00CED1", "circle", 25)

def draw_logo_5():
    draw_logo("A", "purple", "#FF69B4", "square", 30)

def draw_logo_6():
    draw_logo("A", "orange", "#32CD32", "star", 40)

def draw_logo_7():
    draw_logo("A", "cyan", "#7FFFD4", "circle", 35)

def draw_logo_8():
    draw_logo("A", "magenta", "#6A5ACD", "square", 30)

def draw_logo_9():
    draw_logo("A", "black", "#FFDAB9", "star", 25)

def draw_logo_10():
    draw_logo("A", "pink", "#B0E0E6", "circle", 40)

