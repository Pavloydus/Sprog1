seznam = {}

delka1 = int(input("Zadej počet studentů: "))
while delka1 > 0:
    soucet = 0
    znamky = []

    jmeno = input("Zadej jméno: ")

    delka2 = int(input("Zadej počet známek: "))
    while delka2 > 0:
        znamka = int(input("Zadej známku: "))
        znamky.append(znamka)
        delka2 -= 1

    for x in range(len(znamky)):
        soucet += znamky[x]
    prumer = soucet / len(znamky)

    seznam[jmeno] = prumer
    delka1 -= 1

print(f"Výsledky: {seznam}")