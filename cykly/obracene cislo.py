x = input("Zadej číslo: ")

obr = 0
cif = 1
for i in range(len(x)):
    obr += int(x[i]) * cif
    cif *= 10
print(f"Obrácené číslo: {obr}")