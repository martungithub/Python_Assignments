def zip(data1, data2):
    new_list = []
    pairs = []
    if len(data1) != len(data2):
        return "List are not equals"
    else:
        for i in range(len(data1)):
            pairs.append(data1[i])
            pairs.append(data2[i])
            new_list.append(pairs)
            pairs = []
    return new_list


print(zip([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
