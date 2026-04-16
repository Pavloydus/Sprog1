zaklad = int(input("Zadej základ: "))
exponent = int(input("Zadej exponent: ")) - 1

vysledek = zaklad

while exponent > 0:
    vysledek *= zaklad
    exponent -= 1

print(f"Výsledek je {vysledek}")