import random

delka = int(input("Zadej délku seznamu: "))

seznam = []
unikat = []
delka2 = 0

for i in range(delka):
    cislo = random.randint(1, 100)
    seznam.append(cislo)

for x in range(delka):
    if delka2 == 0:
        unikat.append(seznam[x])
        delka2 +=1
    else:
        pravda = 0
        for y in range(delka2):
            if seznam[x] == unikat[y]:
                pravda = 1
        if pravda == 0:
            unikat.append(seznam[x])
            delka2 += 1

print(unikat)