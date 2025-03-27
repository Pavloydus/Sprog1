text = input("Zadej text: ")
pocitadlo = {}

seznam = text.split(" ")

for slovo in seznam:
    if slovo in pocitadlo:
        pocitadlo[slovo] += 1
    else:
        pocitadlo[slovo] = 1

print(pocitadlo)