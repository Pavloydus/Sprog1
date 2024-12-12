#Vstup
print("Zadej tři čísla: ")
číslo1 = float(input("Číslo 1: "))
číslo2 = float(input("Číslo 2: "))
číslo3 = float(input("Číslo 3: "))

# Výstup
if číslo2 < číslo1:
    max = číslo1
else:
    max = číslo2
    mid = číslo1
if max < číslo3:
    min = mid
    mid = max
    max = číslo3
