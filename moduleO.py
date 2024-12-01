# moduleO.py
import turtle
from decorations import *
import random


def draw_letter_o(x, y, font_size, font):
    """Writes the letter 'O' with a specific font family and size."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(random_color())  # Set a random color for the text
    turtle.write(
        "O", 
        align="center", 
        font=(font, font_size, "bold")  # Bold styling for the letter
    )

def style_letter_with_decorations(x, y):
    FONT = random_font()
    turtle.speed(0)
    turtle.bgcolor(random_color())
    turtle.hideturtle()

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
    turtle.color(random_color())
    draw_letter_o(x + shadow_offset, y - shadow_offset, 150 , FONT)
    draw_letter_o(x, y, 150,FONT)

def draw_logo_1():
    style_letter_with_decorations(0, 0)
