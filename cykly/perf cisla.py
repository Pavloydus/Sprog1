for x in range(1, 10001):
    perf = 0
    for delitel in range(1, x-1):
        if x % delitel == 0:
            perf += delitel
    if x == perf:
        print(f"Číslo {x} je perfektní.")