x = input("Zadej číslo: ")

obr = 0
cif = 1
for i in range(len(x)):
    obr += int(x[i]) * cif
    cif *= 10
if int(x) == obr:
    print(f"Číslo {x} je palindrom")
else:
    print(f"Číslo {x} není palindrom")