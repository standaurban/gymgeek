import turtle
turtle.shape("turtle")
turtle.colormode(255)
turtle.color(102, 153, 153)
delsi = 300
kratsi = delsi / 10
turtle.penup()
turtle.goto(-delsi/2, delsi/10 * 10)
turtle.pendown()
for i in range(10):
    turtle.forward(delsi)
    turtle.right(90)
    turtle.forward(kratsi)
    turtle.right(90)
    turtle.forward(delsi)
    turtle.left(90)
    turtle.forward(kratsi)
    turtle.left(90)
turtle.forward(delsi)    

