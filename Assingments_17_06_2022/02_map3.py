def map3(funct, data1, data2, data3):
    res = []
    for i in range(3):
        res.append(funct(data1[i], data2[i], data3[i]))
    return res


def sum(data1, data2, data3):
    return data1 + data2 + data3


lst1 = [1, 2, 3]
lst2 = [10, 20, 30]
lst3 = [100, 200, 300, 400]
print(map3(sum, lst1, lst2, lst3))
