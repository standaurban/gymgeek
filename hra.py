from random import randrange
print("Hádej číslo. Máš 6 pokusů.")

MAX = 100
number = randrange(MAX) + 1
remaining_attempts = 6
guess = None

def get_remaining_attempts():
    if remaining_attempts == 1:
        return "zbývá 1 pokus"
    elif remaining_attempts < 6:
        return "zbývají %d pokusy" % remaining_attempts
    else:
        return "zbývá %d pokusů" % remaining_attempts
    

def get_guess():
    while True:
        n = input("Hádej číslo od 1 do %d: (%s)" % (MAX, get_remaining_attempts()))

        if n.isnumeric():
            n = int(n)

            if 1 <= n <= MAX:
                return n

        print("Špatně zadaný vstup!")

#Hl. cyklus
while remaining_attempts > 0 and guess != number:
    guess = get_guess()
    if guess > number:
        print("Moc velký")
    elif guess < number:
        print("Moc malý")
    remaining_attempts -= 1

#Vyhodnocení hry
if guess == number:
    print("Vyhrál jsi")
else:
    print("Prohrál jsi. Moje číslo bylo %d: " %number)


