import turtle
import random

size = 100

turtle.shape("turtle")
turtle.color(1, 153/255, 1)
turtle.pensize(3)
for y in range(100):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.left(40)
    for i in range(5):
        turtle.forward(10)
        turtle.left(size - (size*2) / size)

    

##def nuhelnik(strana = 20, pocet = 100) :
##    uhel = 180 * (pocet-2) / pocet
##    for i in range(pocet):
##        Stanik.forward(strana)
##        Stanik.left(180-uhel)
##nuhelnik()
##
###Stanik.shape("turtle")
#Stanik.color(255/255, 153/255, 255/255)

#for _ in range(4):
    #Stanik.forward(size)
    #Stanik.left(90)
