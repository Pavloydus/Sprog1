pocet = int(input("Zadej počet lidí: "))
k = int(input("Zadej skok: "))

seznam = []
for x in range(pocet):
    seznam.append(x + 1)

def hra(seznam, kolo):
    if len(seznam) > 1:
        seznam2 = seznam[k:len(seznam)]
        seznam2.extend(seznam[0:k])
        if k < len(seznam):
            seznam2.remove(seznam[k-1])
            print(seznam2)
            hra(seznam2, kolo)
        else:
            seznam2.remove(seznam[(k - kolo * len(seznam))-1])
            print(seznam2, kolo)
            hra(seznam2, kolo+1)
    else:
        print(seznam)
        return
    
hra(seznam, 1)