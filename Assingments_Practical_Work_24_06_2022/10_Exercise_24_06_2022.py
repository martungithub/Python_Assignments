def same_parity(n, *args):
    arguments = [i for i in args if i % n == 0]
    return arguments


print(same_parity(5, 10, 2, 4, 35, 7, 25, 50, 4, 8))
