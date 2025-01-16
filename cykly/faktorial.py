# Vstup
číslo = int(input("Zadej přirozené číslo: "))
x = číslo

# Výstup
faktoriál = 1
while x > 0:
    faktoriál *= x
    x -= 1

print(f"Faktoriál čísla {číslo} je {faktoriál}.")