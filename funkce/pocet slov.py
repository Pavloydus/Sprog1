def pocitani_slov(text, min_delka=3):
    sez_veta = text.split(" ")
    slovnik = {}
    for x in range(len(sez_veta)):
        if len(sez_veta[x]) >= min_delka:
            if sez_veta[x] in slovnik:
        


veta = str(input("Zadej větu: "))
delka = int(input("Zadej minimální délku slova: "))

print(pocitani_slov(veta, delka))