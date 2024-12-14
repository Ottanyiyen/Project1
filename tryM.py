from turtle import *

setup(500, 500)

hideturtle()
bgcolor('#B85042')
pencolor('#210070')
right(90)

pos = [(-105, 90), (60, 90)]
for x, y in pos:
    up()
    goto(x, y)
    down()
    fillcolor('#210070')
    begin_fill()
    for _ in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()
up()
goto(-105, 90)
down()
left(22)

begin_fill()
for _ in range(2):
    forward(217)
    left(68)
    forward(40)
    left(112)
end_fill()

up()
goto(60, 90)
down()
right(44)

begin_fill()
for _ in range(2):
    forward(217)
    left(112)
    forward(40)
    left(68)
end_fill()

exitonclick()