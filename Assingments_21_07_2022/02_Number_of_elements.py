def num_of_elements(lst):
    # We have to skip the first element because dividing by zero is undefined
    count = 0
    for i in range(1, len(lst)):
        if lst[i] % i == 0:
            count += 1
    return count


elements = [1, 5, 4, 7, 15, 20, 35, 40, 45, 78, 11, 9, 12]
print(num_of_elements(elements))
