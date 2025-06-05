n = 0
presnost = 0

def vyhled(x, prev, pocet):
    if x * x == n or pocet == presnost:
        print(x, x * x)
        return
    elif (x * x) < n:
        vyhled(x + (abs(x - prev)) / 2, x, pocet + 1)
    else:
        vyhled(x - (abs(x - prev)) / 2, x, pocet + 1)

n = int(input("Zadej hledané číslo: "))
presnost = int(input("Zadej přesnost: "))
vyhled(n / 2, n, 1)