def slouceni_bez_prepisu(prvni, druhy):
    for x in druhy:
        if prvni.get(x) == None:
            prvni[x] = druhy[x]
    return prvni

# Příklad použití
print(slouceni_bez_prepisu({"a": 1, "b": 2}, {"b": 99, "c": 3}))
# Očekávaný výstup: {'a': 1, 'b': 2, 'c': 3}

print(slouceni_bez_prepisu({}, {"a": 1, "b": 2}))
# Očekávaný výstup: {'a': 1, 'b': 2}

print(slouceni_bez_prepisu({"a": 1, "b": 2}, {"a": 99, "b": 99}))
# Očekávaný výstup: {'a': 1, 'b': 2}