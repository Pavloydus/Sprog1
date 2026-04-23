import random

delka = int(input("Zadej délku seznamu: "))
delka_rand = delka

seznam = []

while delka_rand > 0:
    seznam.append(random.randint(0, delka**2))
    delka_rand -= 1

for i in range(delka):
    for x in range(delka - 1):
        if seznam[x] > seznam[x + 1]:
            seznam[x], seznam[x + 1] = seznam[x + 1], seznam[x]

print(seznam)