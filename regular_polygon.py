
import turtle
n = int(input("Zadej celé a přirozené číslo: "))
if n >= 2:
    for i in range(n):
        turtle.forward(50)
        turtle.left(((2/n)*180))
else:
    exit()
#úprava aby jsem mohl změnit komentář na githubu

