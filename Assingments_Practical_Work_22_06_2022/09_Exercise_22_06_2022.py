def is_sublist(data1, data2):
    new_list = [[]]
    for i in range(len(data1) + 1):
        for k in range(i):
            new_list.append(data1[k: i])
    for i in new_list:
        if data2 in new_list:
            return True
        else:
            return False

print(is_sublist([1, 2, 3, 4, 5], [2, 3,4]))
