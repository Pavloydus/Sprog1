import math

# Vstup
v = float(input("Výška (v cm): "))
r = float(input("Poloměr (v cm): "))

# Povrch
S = round(2 * math.pi * r * (r + v), 2)
# Objem
V = round(math.pi * (r ** 2) * v, 2)

# Výstup
print(f"Povrch válce: {S} cm**2")
print(f"Objem válce: {V} cm**3")