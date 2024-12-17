from turtle import *
setup(500, 500)



hideturtle()
bgcolor('#A72218')
pencolor('#E9E7E0')
fillcolor('#E9E7E0')
right(90)

up()
goto(-105, 90)
down()
left(22)

begin_fill()
for _ in range(2):
    forward(200)
    left(68)
    forward(40)
    left(112)
end_fill()

up()
goto(46, 90)
down()
right(44)

begin_fill()
for _ in range(2):
    forward(200)
    left(112)
    forward(40)
    left(68)
end_fill()




exitonclick()

