def remove_all(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            data.remove(value)
        i += 1
    return data


data_list = [1, 2, 3, 4, 5, 4, 7]
print(remove_all(data_list, 4))
