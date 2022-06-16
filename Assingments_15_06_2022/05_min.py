def min(data):
    minimum = data[0]
    i = 0
    while i < len(data):
        if data[i] <= minimum:
            minimum = data[i]
        i += 1
    return minimum


new_list = [2, 5, 6, -25, 7, 20, -10]
print(min(new_list))
