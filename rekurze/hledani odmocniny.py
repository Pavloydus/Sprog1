n = 0
presnost = 900

def vyhled(x, pocet):
    if x * x == n or pocet == presnost:
        print(x, x * x)
        return
    elif (x * x) < n:
        vyhled(x * (n - (x * x)), pocet + 1)
    else:
        vyhled(x / (1.1 - (1 / pocet)), pocet + 1)

n = int(input("Zadej hledané číslo: "))
vyhled(n / 2, 1)

# 4.5 * 4.5 > 9
# 2.25 * 2.25 < 9
# 3.4 * 3.4 > 9
# 1.7 * 1.7 < 9
# 3.4