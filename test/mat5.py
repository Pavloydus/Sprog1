def nejlepsi_student(zaci):
    nej_prumer = 6
    for zak in zaci:
        zaci[zak] = sum(zaci[zak])/len(zaci[zak])
        if zaci[zak] < nej_prumer:
            nej_prumer = zaci[zak]
            nej_zak = zak
    return nej_zak

# Příklad použití
zaci = {
    "Adam":  {"znamky": [1, 2, 1]},
    "Bára":  {"znamky": [3, 4, 3]},
    "Cyril": {"znamky": [1, 1, 1]},
}
print(nejlepsi_student(zaci))  # Očekávaný výstup: Cyril

zaci2 = {
    "Zuzana": {"znamky": [2, 2, 2]},
    "Adam":   {"znamky": [2, 2, 2]},
}
print(nejlepsi_student(zaci2))  # Očekávaný výstup: Adam (remíza, abecedně)
