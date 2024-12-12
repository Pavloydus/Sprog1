# Vstup
C = float(input("Teplota (v °C): "))

# Výpočet
K = C + 273.15
F = C * 9/5 + 32

# Výstup
print(f"Teplota: {round(K, 2)} K, {round(F, 2)} F")