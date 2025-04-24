def nejdelsi_slovo(text):
    sez_veta = text.split(" ")
    max = 0
    for x in sez_veta:
        if len(x) > max:
            max = len(x)
            nej = x
    return nej

veta = str(input("Zadej větu: "))
print(f"Nejdelší slovo: {nejdelsi_slovo(veta)}")