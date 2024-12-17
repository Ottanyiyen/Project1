from turtle import *
setup(500,500)


hideturtle()
bgcolor('#404041')
pencolor('#E6C17A')
fillcolor('#E6C17A')

pos = [(-125, 100), (-120, -90)]
for x, y in pos:
    up()
    goto(x, y)
    down()
    begin_fill()
    for _ in range(2):
        forward(250)
        left(120)
        forward(40)
        left(60)
    end_fill()
up()
goto(99, 132)
down()
right(142)

begin_fill()
for _ in range(2):
    forward(302)
    left(90)
    forward(40)
    left(90)
end_fill()

exitonclick()