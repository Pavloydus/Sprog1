def bubble1(seznam, skip=0, step=0):
    for x in range(len(seznam)-1-skip):
        step += 1
        if seznam[x] > seznam[x+1]:
            prehoz = seznam[x]
            seznam[x] = seznam[x+1]
            seznam[x+1] = prehoz
        print(seznam)
    skip += 1
    print(step)
    if skip == (len(seznam)-2):
        return seznam, step
    else:
        bubble1(seznam, skip, step)