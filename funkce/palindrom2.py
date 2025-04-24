def palindrom(slovo):
    slovo = slovo.lower()
    return slovo == slovo[::-1]

zadane = str(input("Zadej slovo: "))

print(palindrom(zadane))