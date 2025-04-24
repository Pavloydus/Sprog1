def pocitani_slov(text, min_delka=3):
    text = text.lower()
    if text[-1] in ".,;:!?-":
        text = text[:-1]

    sez_veta = text.split(" ")
    slovnik = {}

    for x in sez_veta:
        if len(x) >= min_delka:
            if x in slovnik:
                slovnik[x] += 1
            else:
                slovnik[x] = 1
    return slovnik


veta = str(input("Zadej větu: "))
delka = int(input("Zadej minimální délku slova: "))

print(pocitani_slov(veta, delka))