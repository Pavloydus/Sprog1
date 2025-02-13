for x in range(1, 10001):
    del1 = 0
    del2 = 0
    for delitel in range(1, x-1):
        if x % delitel == 0:
            del1 += delitel
    delitel = 0
    for delitel in range(1, del1-1):
        if del1 % delitel == 0:
            del2 += delitel
    if x == del2 and x != del1:
        print(f"Čísla {x} a {del1} jsou přátelská.")
