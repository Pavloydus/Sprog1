import math

# Vstup
v = float(input("Výška (v cm): "))
r = float(input("Poloměr (v cm): "))

# Povrch
S = 2 * math.pi * r * (r + v)
# Objem
V = math.pi * (r ** 2) * v

# Výstup
print(f"Povrch válce: {round(S, 2)} cm**2")
print(f"Objem válce: {round(V, 2)} cm**3")