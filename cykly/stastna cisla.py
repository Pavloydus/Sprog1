for x in range(101):
    while x != 4 and x != 1:
        soucet = 0
        for delka in range(len(str(x))):
            soucet += int(x)**int(str(x)[delka])
        x = soucet
    if x == 1:
        print(x)