seznam = []

def vypis_suda_od_do(od, do):
    for x in range(od, do):
        if x % 2 == 0:
            seznam.append(x)


zacatek = int(input("Zadej začátek: "))
konec = int(input("Zadej konec: "))

if zacatek < konec:
    vypis_suda_od_do(zacatek, konec)
    print(f"Seznam: {seznam}")
else:
    print("Začátek je větší než konec!")