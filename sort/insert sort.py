seznam = [4, 2, 9, 7, 3]

def place(cislo, x, skip):
    if cislo < seznam[x-skip] and (x-skip) >= 0:
        place(cislo, x, skip + 1)
    else:
        for y in range(sorted):
            shift = seznam[x-skip+1]
            seznam[x-skip+1] = cislo
            

        return

def insert1(sorted=1, ):
    while sorted != len(seznam):
        place(seznam[sorted], sorted, 1)
        sorted += 1
