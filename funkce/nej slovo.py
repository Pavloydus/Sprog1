def nejdelsi_slovo(text):
    sez_veta = text.split(" ")
    max = 0
    while len(sez_veta) > 0:
        if len(sez_veta[0]) > max:
            max = len(sez_veta[0])
            nej = sez_veta.pop(0)
        else:
            sez_veta.remove(sez_veta[0])
    return nej

veta = str(input("Zadej větu: "))
print(f"Nejdelší slovo: {nejdelsi_slovo(veta)}")