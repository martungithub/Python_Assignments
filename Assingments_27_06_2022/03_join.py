def join(data, sep):
    res = ""
    for i in range(len(data)):
        if i == len(data) - 1:
            res += str(data[i])
        else:
            res += str(data[i]) + sep
    return res


print(join([1, 2, 3, 4, 5, 6], ''))
