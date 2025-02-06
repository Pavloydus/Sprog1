for x in range(101):
    promstr = str(x)
    y = 0
    while y != 4 and y != 1 and x < 101:
        y = 0
        for delka in range(len(promstr)):
            y += int(promstr)**int(promstr[delka])
        promstr = str(y)
        if y == 1:
            print(y)