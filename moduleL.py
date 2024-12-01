from turtle import *
from decorations import *

def draw_logo_l():
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
    pencolor(random_color())
    hideturtle()
    
    # Vertical line of L
    up()
    goto(-100, -100)
    down()
    setheading(90)
    fillcolor(random_color())
    begin_fill()
    forward(200)
    right(90)
    forward(40)
    right(90)
    forward(200)
    right(90)
    forward(40)
    end_fill()
    
    # Horizontal line of L
    up()
    goto(-100, -100)
    down()
    setheading(0)
    begin_fill()
    forward(160)
    right(90)
    forward(40)
    right(90)
    forward(160)
    right(90)
    forward(40)
    end_fill()
