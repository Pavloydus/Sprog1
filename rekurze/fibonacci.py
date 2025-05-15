def fib(n):
    cisla = [0]
    if n > 1:
        cislo = fib(n-1) + cisla[n-2]
        cisla.append(cislo)
        return cislo
    else:
        return n

cislo = int(input("Zadej číslo: "))
print(fib(cislo))