def spolDel(cislo, zbytek):
    if zbytek == 0:
        print(cislo)
        return
    else:
        spolDel(zbytek, cislo % zbytek)

cis1 = int(input("Zadej číslo: "))
cis2 = int(input("Zadej číslo: "))

spolDel(cis1, cis2)