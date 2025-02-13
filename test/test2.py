soucet = 0
mocnina = 0

for x in range(1,101):
    soucet += x**2
    mocnina += x

print(f"Rozdíl je {mocnina**2 - soucet}")