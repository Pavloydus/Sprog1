def vytvor_trojuhelnik1(n):
    trojuhelnik = ""

    #přidávání hvězdiček
    for delka in range(n):
        for i in range(delka+1):
            trojuhelnik += "*"

        #line break na konci
        if delka < n-1:
            trojuhelnik += "\n"

    return trojuhelnik


def vytvor_trojuhelnik2(n):
    trojuhelnik = ""

    for delka in range(n):
        #počet mezer
        for i in range(n - delka - 1):
            trojuhelnik += " "
        
        #počet hvězdiček
        for i in range(2*(delka+1)-1):
            trojuhelnik += "*"

        #line break na konci
        if delka < n-1:
            trojuhelnik += "\n"

    return trojuhelnik


def vytvor_trojuhelnik3(n):
    trojuhelnik = ""

    for delka in range(n-1):
        #počet mezer na začátku
        for i in range(n - delka - 1):
            trojuhelnik += " "
        
        #hvězdičeky na okraji vnitřních mezer
        for mezera in range(2*(delka+1)-1):
            if mezera == 0 or mezera == 2*(delka+1)-2:
                trojuhelnik += "*"
            else:
                trojuhelnik += " "

        #line break na konci
        trojuhelnik += "\n"
    
    #poslední řádek
    for i in range(2*n-1):
        trojuhelnik += "*"

    return trojuhelnik

def vytvor_trojuhelnik2(n):
    trojuhelnik = ""

    for delka in range(n):
        #počet mezer
        for i in range(n - delka - 1):
            trojuhelnik += " "
        
        #počet hvězdiček
        for i in range(2*(delka+1)-1):
            trojuhelnik += "*"

        #line break na konci
        if delka < n-1:
            trojuhelnik += "\n"

    return trojuhelnik


def vytvor_ctverec(n):
    ctverec = ""

    #první řádek
    for i in range(n):
        ctverec += "*"
    ctverec += "\n"

    for i in range(n-2):
        #hvězdičeky na okraji vnitřních mezer
        for sloupec in range(n):
            if sloupec == 0 or sloupec == n-1:
                ctverec += "*"
            else:
                ctverec += " "

        #line break na konci
        ctverec += "\n"
    
    #poslední řádek
    for i in range(n):
        ctverec += "*"

    return ctverec
print(vytvor_ctverec(5))