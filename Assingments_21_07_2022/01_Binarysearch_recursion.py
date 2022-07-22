def binsearch(lst, start, end, key):
    mid = (start + end) // 2
    if end <= start:
        return -1
    elif lst[mid] == key:
        return mid
    elif lst[mid] < key:
        return binsearch(lst, mid + 1, end, key)

    else:
        return binsearch(lst, start, mid, key)


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binsearch(elements, 0, len(elements), 1))
# print(binsearch(lst, 0, len(lst), 9))
# print(binsearch(lst, 0, len(lst), 25))
