def partition(left, right, seznam):
    mid = round((left + right)/2)
    pivot = seznam[mid]
    while True:
        while seznam[left] < pivot:
            left += 1
        while seznam[right] > pivot:
            right -= 1
        print(left, right)
        if left < right:
            seznam[left], seznam[right] = seznam[right], seznam[left]
            left += 1
            right -= 1
            print(seznam)
        else:
            print(seznam)
            break
    return left, right


def quick1(seznam):
    left = 0
    right = len(seznam)-1
    left, right = partition(left, right, seznam)
    while right - left > 0:
        left, right = partition(0, left-1, seznam)
    

print(partition(0, 9, [1, 8, 6, 44, 11, 7, 9, 46, 8, 2]))