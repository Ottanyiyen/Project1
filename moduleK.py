# moduleK.py
import turtle
from decorations import *
import random

def draw_letter_k(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(12)
    turtle.color(random_color())

    # Draw the main body of the K
    turtle.setheading(90)  # Point up
    turtle.forward(size)
    turtle.backward(size // 2)
    turtle.setheading(45)
    turtle.forward(size // 1.5)
    turtle.backward(size // 1.5)
    turtle.setheading(-45)
    turtle.forward(size // 1.5)

def style_letter_with_decorations(x, y):
    """Adds decorations and draws the letter with effects."""
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor(random_color())
    # Add decorations
    for _ in range(random.randint(5, 15)):  # Random stars
        draw_star(
            random.randint(-200, 200),
            random.randint(-200, 200),
            random.randint(10, 30),
            random_color(),
        )

    for _ in range(random.randint(1, 10)):  # Random circles
        draw_circle_pattern(random.randint(-100, 300), random.randint(-100, 300), random.randint(1, 10), random_color())

    draw_rectangle(random_color())
    draw_triangle(random_color())
    
    # Add shadow effect
    shadow_offset = 4
    turtle.color("gray")
    draw_letter_k(x + shadow_offset, y - shadow_offset, 150)
    draw_letter_k(x, y, 150)

def draw_logo_1():
    style_letter_with_decorations(0, 0)

