def palindrom(slovo):
    obracene = slovo[::-1]
    if obracene == slovo:
        return True
    else:
        return False

zadane = str(input("Zadej slovo: "))

print(palindrom(zadane))