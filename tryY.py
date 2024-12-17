from turtle import *
setup(500, 500)





hideturtle()
bgcolor('#D49A56')
pencolor('#EDE7EA')
fillcolor('#EDE7EA')
right(90)

up()
goto(-82, 150)
down()
left(22)

begin_fill()
for _ in range(2):
    forward(150)
    left(40)
    forward(40)
    left(140)
end_fill()

up()
goto(40, 133)
down()
right(44)

begin_fill()
for _ in range(2):
    forward(150)
    left(140)
    forward(40)
    left(40)
end_fill()

up()
goto(8, 53)
down()

begin_fill()
for _ in range(2):
    forward(200)
    left(140)
    forward(40)
    left(40)
end_fill()




exitonclick()

