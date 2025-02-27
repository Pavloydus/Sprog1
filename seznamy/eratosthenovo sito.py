n = int(input("Zadej číslo:  "))

prvocisla = []
seznam = []
for cislo in range(n):
    seznam.append(cislo)

for x in range(n):
    prvocisla.append(seznam.pop(x))
    for y in range(len(prvocisla)):
        if seznam[x]