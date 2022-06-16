def pop(data, i):
    if i == "None" or i == len(data) - 1:
        value = data[-1]
        data = data[:-1]
        return value

    elif i > 0 and i >= len(data) or 0 > i < -len(data):
        raise ValueError('pop index out of range')

    else:
        before_i = data[:i]
        after_i = data[i + 1:]
        answer = before_i + after_i
        return data[i]


new_list = [1, 2, 3, 4, 5]
print(pop(new_list, 2))
# print(pop(new_list, -6))
# print(pop(new_list, 8))
