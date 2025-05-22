#slovo od uživatele (Ahoj)
#pismena nahodne prohazet (hAjo)

import random

def prehoz(char, slovo):
    rnd = random.randint(0, 1)
    if rnd == 0:
        slovo = slovo + char
    else:
        slovo = char + slovo
    return slovo

zadane = input("Zadej slovo: ")
delka = len(zadane)
vysledek = ""

for x in zadane:
    vysledek = prehoz(x, vysledek)

print(vysledek)