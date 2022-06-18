def map2(funct, data1, data2):
    res = []
    for i in range(len(data1)):
        res.append(funct(data1[i], data2[i]))
    return res


def pow(data1, data2):
    return data1 ** data2


base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map2(pow, base, exp))
