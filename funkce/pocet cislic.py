def pocet_cislic(n):
    x = str(abs(n))
    if n % 1 == 0:
        delka = len(x) - 2
    else:
        delka = len(x) - 1
    return delka

cislo = float(input("Zadej číslo: "))

print(f"Počet číslic: {pocet_cislic(cislo)}")