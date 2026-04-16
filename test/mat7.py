cislo = float(input("Zadej základ: "))
if cislo >= 1 and cislo.is_integer():
    vysledek = int(cislo)
    x = int(cislo) - 1

    while x >= 1:
        vysledek *= x
        x -= 1

    print(f"Faktoriál čísla {int(cislo)} je {vysledek}")
else:
    print("chcípni")