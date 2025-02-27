delka = int(input("Délka seznamu: "))
seznam = []

print("Zadej seznam: ")
while delka > 0:
    seznam.append(int(input))
    delka -= 1

od = int(input("Dolní hranice intervalu: "))
do = int(input("Horní hranice intervalu: "))

print(seznam[od:do])

