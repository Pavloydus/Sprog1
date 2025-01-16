# Vstup
číslo = int(input("Zadej přirozené číslo: "))
x = 2

# Výstup
while x < číslo:
    if číslo % x == 0:
        print (f"Číslo {číslo} není prvočíslo.")
        break
    x += 1
    

