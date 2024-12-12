# Vstup
objem = float(input("Objem dat (v MB): "))
rychlost = float(input("Rychlost stahování (v Mbit/s): "))

# Výpočet
t = round(objem * 8 / rychlost, 2)

# Výstup
print(f"Doba stahování: {t} s")