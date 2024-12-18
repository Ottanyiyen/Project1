from turtle import *
setup(500,500)



hideturtle()
bgcolor('#144058')
pencolor('#DD671E')
fillcolor('#DD671E')

penup()
goto(-100, -120)
pendown()

begin_fill()
setheading(90)
forward(240)
right(90)
forward(90)
circle(-122, 166)
goto(-100, -120)
end_fill()

penup()
fillcolor('#144058')
pencolor('#144058')

begin_fill()
goto(-44, -50)
pendown()
setheading(90)
forward(100)
setheading(0)
forward(50)
circle(-50, 180)
forward(50)
end_fill()





exitonclick()