# decorations.py
import turtle
import random
import math

def draw_star(x, y, size, color):
    """Draws a star at the given position with a specific size and color."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_circle_pattern(center_x, center_y, radius, color):
        # Calculate the position of each circle using math.cos and math.sin
        x = center_x
        y = center_y
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(radius)  # Draw a small circle
        turtle.end_fill()

def draw_rectangle(color):
    turtle.penup()
    turtle.goto(random.randint(-200, 0), -75)
    turtle.pendown()
    turtle.color(color)
    for _ in range(2):
        turtle.pensize(5)
        turtle.forward(475)
        turtle.left(90)
        turtle.forward(425)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle( color):
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(5)
    for _ in range(3):
        turtle.forward(650)
        turtle.left(120)
    turtle.end_fill()
    
def random_color():
    
    r = random.random()  # Red component (0.0 to 1.0)
    g = random.random()  # Green component (0.0 to 1.0)
    b = random.random()  # Blue component (0.0 to 1.0)
    return (r, g, b)

def random_font():
    fonts = [
        "Arial", "Verdana", "Courier", "Times New Roman", "Comic Sans MS", 
        "Georgia", "Trebuchet MS", "Impact", "Tahoma", "Lucida Console",
        "Palatino Linotype", "Brush Script MT", "Consolas", "Century Gothic", 
        "Monaco", "Courier New", "Monospace" ,"Cursive"]
    return random.choice(fonts)