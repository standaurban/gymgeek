#Doma
nakup = []

for i in range(10) :
    nakup.append(input("Napiš na lístek zboží co potřebuješ : "))

print("Běž na nákup.")

#V obchodě
print("--- OBCHOD ---")

for i in range(len(nakup)):
    zbozi = input("^\___> <- Tvůj košík: ")

    if zbozi in nakup:
        print("OK")
        nakup.remove(zbozi)
    else:
        print("Měl jsi koupit něco jiného.")

print("Ve tvém košíku ^\(° ͜ʖ °)> není toto zboží: ")
for nekoupene_zbozi in nakup:
    print("-", nekoupene_zbozi)

    
