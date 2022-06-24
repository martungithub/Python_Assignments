def even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def get_median(data):
    if not even(len(data)):
        print("The median is: ", data[int(len(data) / 2)])
    else:
        index = int(len(data) / 2 - 1)
        print("The median is: ", (data[index] + data[index + 1]) / 2)


get_median([2, 3, 11, 13, 17, 26, 34, 47, 18, 27])
