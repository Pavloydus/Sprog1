def merging1(seznam1, seznam2, step):
    seznam = []
    i = 0
    j = 0
    while len(seznam) != len(seznam1) + len(seznam2):
        if i < len(seznam1) and j < len(seznam2):
            step += 1
            if seznam1[i] < seznam2[j]:
                seznam.append(seznam1[i])
                i += 1
            else:
                seznam.append(seznam2[j])
                j += 1
        elif i >= len(seznam1):
            seznam.append(seznam2[j])
            j += 1
        else:
            seznam.append(seznam1[i])
            i += 1
    return seznam, step

def re_merge1(seznam, step):
    seznam1 = []
    seznam2 = []
    mid = round(len(seznam)/2)

    for x in range(mid):
        seznam1.append(seznam[x])
    for y in range(mid, len(seznam)):
        seznam2.append(seznam[y])

    if len(seznam1) > 1:
        seznam1, step = re_merge1(seznam1, step)
    if len(seznam2) > 1:
        seznam2, step = re_merge1(seznam2, step)

    return merging1(seznam1, seznam2, step)

def merge1(seznam):
    step = 0
    seznam, step = re_merge1(seznam, step)
    return step


print(merge1([1, 56, 45, 2, 8, 19, 3, 38, 2]))