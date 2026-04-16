import math

cislo = int(input("Zadej číslo: "))
prvocislo = True
if cislo == 1:
    prvocislo = False

for x in range(2, round(math.sqrt(cislo)) + 1):
    if cislo % x == 0:
        prvocislo = False
        break

if cislo == 2:
    prvocislo = True

if prvocislo == True:
    print("yaaaay")
else:
    print("chcípni")