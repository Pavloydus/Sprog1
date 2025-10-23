def partition1(left, right, seznam, step):
    pivot = seznam[round((left + right)/2)]
    while left <= right:
        step += 1
        while seznam[left] < pivot:
            step += 1
            left += 1
        while seznam[right] > pivot:
            step += 1
            right -= 1
        print(left, right)
        step += 1
        if left <= right:
            print(seznam)
            seznam[left], seznam[right] = seznam[right], seznam[left]
            left += 1
            right -= 1
    return left, step

def quick1(left, right, seznam, step):
    step += 1
    if left < right:
        mid, step = partition1(left, right, seznam, step)
        print("aaaaaaaaaaa")
        step = quick1(left, mid-1, seznam, step)
        step = quick1(mid, right, seznam, step)
    return step

print(quick1(0, 10, [1, 8, 6, 44, 11, 12, 7, 9, 46, 8, 2], 0))