seznam = [5, 2, 7, 8, 6]
spravne = 0

while not spravne == (len(seznam)-1):
    spravne = 0
    for x in range((len(seznam)-1)):
        print(seznam)
        if seznam[x] > seznam[x+1]:
            prehoz = seznam[x]
            seznam[x] = seznam[x+1]
            seznam[x+1] = prehoz
        else:
            spravne =+ 1
        print(spravne)

print(seznam)
