def prevod_na_minuty(hodiny, minuty):
    if hodiny > -1 and minuty > -1:
        return 60 * hodiny + minuty
    
hod = int(input("Zadej hodiny: "))
min = int(input("Zadej minuty: "))

print(f"{prevod_na_minuty(hod, min)} minut.")