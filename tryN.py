from turtle import *
setup(500,500)

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

exitonclick()