def frekvence_znaku(text):
    text = text.lower()
    slovnik = {}
    for x in text:
        if slovnik.get(x) == None:
            slovnik[x] = 1
        else:
            slovnik[x] += 1
    if slovnik.get(" ") != None:
        del slovnik[" "]
    return slovnik
    

# Příklad použití
print(frekvence_znaku("hello"))
# Očekávaný výstup: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(frekvence_znaku("Hello World"))
# Očekávaný výstup: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

print(frekvence_znaku(""))
# Očekávaný výstup: {}