def insert1(seznam):
    sorted = 0
    step = 0
    while sorted != len(seznam)-1:
        skip = sorted
        while skip >= 0:
            step += 1
            if seznam[skip] > seznam[skip + 1]:
                shift = seznam[skip]
                seznam[skip] = seznam[skip + 1]
                seznam[skip + 1] = shift
                skip -= 1
            else:
                skip -= 1
                continue
        sorted += 1
    return step