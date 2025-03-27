seznam1 = []
seznam2 = []
seznamfin = []

delka1 = int(input("Zadej délku prvního seznamu: "))
delka1c = delka1

while delka1 > 0:
    seznam1.append(int(input(f"Zadej {delka1c - delka1 + 1} číslo pro první seznam: ")))
    delka1 -= 1

delka2 = int(input("Zadej délku druhého seznamu: "))
delka2c = delka2

while delka2 > 0:
    seznam2.append(int(input(f"Zadej {delka2c - delka2 + 1} číslo pro druhý seznam: ")))
    delka2 -= 1

if delka1c > delka2c:
    maxdel = delka1c
else:
    maxdel = delka2c

for x in range(maxdel):
    if x < delka1c:
        seznamfin.append(seznam1[x])
    if x < delka2c:
        seznamfin.append(seznam2[x])


print(f"Výsledný seznam: {seznamfin}")