def contain(data, val):
    i = 0
    check = 0
    while i < len(data):
        if data[i] == val:
            check = 1
        i = i + 1

    if check == 1:
        return True
    else:
        return False


new_list = [1, 2, 3, 4, 1]
print(contain(new_list, 3))
