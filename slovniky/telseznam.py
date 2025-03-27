seznam = {}

delka = int(input("Zadej počet kontaktů: "))
while delka > 0:
    jmeno = input("Zadej jméno: ")
    cislo = input("Zadej číslo: ")
    seznam[jmeno] = cislo
    delka -= 1

search = input("Koho chceš vyhledat? ")

print(f"Telefonní číslo: {seznam[search]}")