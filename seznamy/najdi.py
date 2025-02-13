seznam = [2, 3, 1, 0, 5, 6, 4, 2]
cislo = int(input("Zadej číslo: "))

print("Číslo se vyskytuje na pozicích: ")

for x in range(len(seznam)):
    if seznam[x] == cislo:
        print(x)