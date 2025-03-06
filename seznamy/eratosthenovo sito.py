n = int(input("Zadej číslo:  "))

prvocisla = []
seznam = []
for cislo in range(n):
    seznam.append(cislo + 1)
seznam.remove(1)

while len(seznam) > 0:
    prvocisla.append(seznam.pop(0))
    for x in seznam:
        if x % prvocisla[-1] == 0:
            seznam.remove(x)
    
print(prvocisla)