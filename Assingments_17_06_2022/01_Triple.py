def map(funct, data):
    return funct(data)


def triple(data):
    new_lst = []

    for i in data:
        new_lst.append(3 * i)
    return new_lst


lst = [1, 2, 3, 4, 5, 6]
print(map(triple, lst))
