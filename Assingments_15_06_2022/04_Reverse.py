def reverse(data):
    i = len(data) - 1
    k = 0
    while k < i:
        temp = data[k]
        data[k] = data[i]
        data[i] = temp
        i -= 1
        k += 1
    return data


list = [1, 2, 3, 4, 5, 5, 4]
print(reverse(list))
