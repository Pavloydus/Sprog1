import time
import random

def merging1(seznam1, seznam2):
    seznam = []
    i = 0
    j = 0
    while len(seznam) != len(seznam1) + len(seznam2):
        if i < len(seznam1) and j < len(seznam2):
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
    return seznam

def re_merge1(seznam):
    seznam1 = []
    seznam2 = []
    mid = round(len(seznam)/2)

    for x in range(mid):
        seznam1.append(seznam[x])
    for y in range(mid, len(seznam)):
        seznam2.append(seznam[y])

    if len(seznam1) > 1:
        seznam1 = re_merge1(seznam1)
    if len(seznam2) > 1:
        seznam2 = re_merge1(seznam2)

    return merging1(seznam1, seznam2)

def merge1(seznam):
    seznam = re_merge1(seznam)
    return

seznam = []
for x in range(50):
    seznam.append(random.randint(-50, 50))

start_me = time.time()
re_merge1(seznam)
end_me = time.time()
time_me = (end_me - start_me)

start_py = time.time()
sorted(seznam)
end_py = time.time()
time_py = (end_py - start_py)

print(time_me, time_py)