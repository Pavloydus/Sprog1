# Vstup
objem = float(input("Objem dat (v MB): "))
rychlost = float(input("Rychlost stahování (v Mbit/s): "))

# Výpočet
t = objem * 8 / rychlost

# Výstup
print(f"Doba stahování: {round(t, 2)} s")