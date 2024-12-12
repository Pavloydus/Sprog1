# Vstup
C = float(input("Teplota (v °C): "))

# Výpočet
K = round(C + 273.15, 2)
F = round(C * 9/5 + 32, 2)

# Výstup
print(f"Teplota: {K} K, {F} F")