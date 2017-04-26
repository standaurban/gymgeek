user = int(input("Zadej číslo pro rozklad: "))
seznam = []
n = 2

while user != 1:
    if user % n == 0:
        seznam.append(n)
        user /= n
    else:
        n += 1
print(seznam)
    
