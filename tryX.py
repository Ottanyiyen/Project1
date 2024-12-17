from turtle import *
setup(500,500)


hideturtle()
bgcolor('#1C5789')
pencolor('#341514')
fillcolor('#341514')
right(90)

up()
goto(-80, 110)
down()
left(40)

begin_fill()
for _ in range(2):
    forward(270)
    left(50)
    forward(34)
    left(130)
end_fill()

up()
goto(55, 110)
down()
left(140)

begin_fill()
for _ in range(2):
    forward(50)
    left(144)
    forward(200)
    left(36)
end_fill()


exitonclick()