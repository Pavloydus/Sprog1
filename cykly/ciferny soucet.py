x = input("Zadej číslo: ")

soucet = 0
for i in range(len(x)):
    soucet += int(x[i])

print(f"Ciferný součet je {soucet}.")