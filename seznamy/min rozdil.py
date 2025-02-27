import random

delka = int(input("Zadej délku seznamu: "))

seznam = []
min = 100

for i in range(delka):
    cislo = random.randint(1, 1000)
    seznam.append(cislo)

for x in range(delka):
    for y in range(delka):
        if x == y:
            break
        else:
            if abs(seznam[x] - seznam[y]) < min :
                min = abs(seznam[x] - seznam[y])

print(min)