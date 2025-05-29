seznam = [1,2,3,5,5,6,7,8,21]
vyhledavane = 0

def vyhled(od, do):
    x = round((od + do)/2)
    if x == od or x == do:
        print("Nenachází se")
        return
    if seznam[x] == vyhledavane:
        print(x)
    elif seznam[x] < vyhledavane:
        vyhled(x, do)
    else:
        vyhled(od, x)

vyhledavane = int(input("Zadej hledané číslo: "))
vyhled(0, len(seznam))