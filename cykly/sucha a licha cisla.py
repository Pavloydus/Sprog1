# Vstup
číslo = int(input("Zadej mez: "))

# Výstup
for x in range(číslo):
    if x % 2 == 0:
        print(f"Číslo {x} je sudé.")
    else:
        print(f"Číslo {x} je liché.")