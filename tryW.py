from turtle import *

setup(500, 500)





hideturtle()
bgcolor('#F52549')
pencolor('#FA6775')
fillcolor('#FA6775')
left(112)

up()
goto(-30, -100)
down()

begin_fill()
for _ in range(2):
    forward(217)
    left(68)
    forward(40)
    left(112)
end_fill()

up()
goto(30, -100)
down()
right(44)

begin_fill()
for _ in range(2):
    forward(217)
    right(68)
    forward(40)
    right(112)
end_fill()

up()
goto(-30, -100)
down()
left(2)

begin_fill()
for _ in range(2):
    forward(140)
    left(110)
    forward(40)
    left(70)
end_fill()

up()
goto(70, -100)
down()
left(41)

begin_fill()
forward(141)
left(110)
forward(40)
left(70)
forward(112)
end_fill()







exitonclick()