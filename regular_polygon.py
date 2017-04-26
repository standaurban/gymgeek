import turtle

def regular_polygon(delka, n):
    for i in range(n):
        turtle.forward(delka)
        turtle.left(((2/n)*180))
        
n = int(input("Zadej celé a přirozené číslo: "))
if n >= 2:
    regular_polygon(80, n)    
else:
    exit()



