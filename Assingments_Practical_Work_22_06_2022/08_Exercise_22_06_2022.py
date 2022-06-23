def is_increasing(data):
    initial_data = []
    [initial_data.append(i) for i in data]

    for i in range(len(data)):
        for k in range(len(data)):
            if data[i] < data[k]:
                data[k], data[i] = data[i], data[k]

    if initial_data == data:
        return True
    else:
        return False


the_list = [1, 2, 7, 5]
if is_increasing(the_list):
    print("The list has already sorted!")
else:
    print(is_increasing([1, 2, 3, 5]))
