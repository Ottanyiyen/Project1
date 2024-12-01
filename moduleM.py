from turtle import *
from decorations import *

def draw_logo_m_1():
    pencolor(random_color())
    bgcolor(random_color())  # Coral background
    hideturtle()
    turtle.speed(0)
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
    
    # Vertical lines
    pos = [(-160, -100), (-80, -100), (0, -100)]
    for x, y in pos:
        up()
        goto(x, y)
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
    
    # Diagonal connections
    up()
    goto(40, 100)
    down()
    setheading(180)
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

    up()
    goto(-160,140)
    down()
    setheading(90)
    fillcolor(random_color())
    begin_fill()
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    end_fill()
