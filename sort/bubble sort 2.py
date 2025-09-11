seznam = [5, 2, 7, 8, 6, 1]

def bubble(skip, step):
    for x in range(len(seznam)-1):
        print(seznam)
        step += 1
        if seznam[x] > seznam[x+1]:
            prehoz = seznam[x]
            seznam[x] = seznam[x+1]
            seznam[x+1] = prehoz
    skip += 1
    print(step)
    if skip == (len(seznam)-2):
        return seznam
    else:
        bubble(skip, step)

print(bubble(0, 0))