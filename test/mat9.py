import random

delka = int(input("Zadej délku seznamu: "))
delka_rand = delka

seznam = []
unik_seznam = []

while delka_rand > 0:
    seznam.append(random.randint(0, round(delka/3)))
    delka_rand -= 1


for x in range(delka):
    unikat = True

    #kontrola unikatniho seznamu
    for y in range(len(unik_seznam)):
        if seznam[x] == seznam[y]:
            unikat = False 
            break

    #kontrola zbytku seznamu
    for z in range(x+1, delka):
        if seznam[x] == seznam[z]:
            unikat = False
            break

    #pokud zustane True => pridat
    if unikat == True:
        unik_seznam.append(seznam[x])

print(unik_seznam)