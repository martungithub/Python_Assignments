def max(data):
    maximum = data[0]
    i = 0
    while i < len(data):
        if data[i] >= maximum:
            maximum = data[i]
        i += 1
    return maximum


new_list = [-2, -5, -6, -1, -7, -20, -10]
print(max(new_list))
