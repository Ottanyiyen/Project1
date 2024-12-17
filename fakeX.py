import turtle


pen = turtle.Turtle()
pen.hideturtle()


def configure_pen(pen, pcolor, x, y, bg_color):
    pen.color(pcolor)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    turtle.bgcolor(bg_color)






def draw_logo_1():

    configure_pen(pen, "#ca0c0c", -60, -100, "#9e6b6b")
    pen.write("X", font=("Roboto", 150, "bold"))



def draw_logo_2():

    configure_pen(pen, "#ff6600", -60, -100, "#2c8212")
    pen.write("X", font=("Arial", 150, "italic"))



def draw_logo_3():

    configure_pen(pen, "#2e330a", -60, -100, "#9a74c8")
    pen.write("X", font=("Open Sans", 150, "normal"))



def draw_logo_4():

    configure_pen(pen, "#ef9b0b", -60, -100, "#170826")
    pen.write("X", font=("Montserrat", 150, "bold"))



def draw_logo_5():

    configure_pen(pen, "#97b7c4", -60, -100, "#272730")
    pen.write("X", font=("Poppins", 150, "italic"))


def draw_logo_6():

    configure_pen(pen, "#6b1414", -60, -100, "#505477")
    pen.write("X", font=("Arial", 150, "bold"))



def draw_logo_7():

    configure_pen(pen, "#dbf556", -60, -100, "#ad5c97")
    pen.write("X", font=("Inter", 150, "italic"))



def draw_logo_8():

    configure_pen(pen, "#3b4c34", -60, -100, "#a8451a")
    pen.write("X", font=("Oswald", 150, "italic"))



def draw_logo_9():

    configure_pen(pen, "#1d430f", -60, -100, "#943fd9")
    pen.write("X", font=("Agu Display", 150, "bold"))



def draw_logo_10():

    configure_pen(pen, "#8798de", -60, -100, "#19460c")
    pen.write("X", font=("Playfair Display", 150, "normal"))
