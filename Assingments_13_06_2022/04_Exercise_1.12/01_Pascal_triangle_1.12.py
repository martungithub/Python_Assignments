def factorial(n):
    res = 1
    counter = 1
    while counter <= n:
        res = res * counter
        counter = counter + 1
    return res


def pascal_triangle(row):
    k = 0
    if row == 0:
        print(1)

    while k != row + 1:
        print(int(factorial(row) / (factorial(k) * factorial(row - k))), end=" ")
        k += 1


pascal_triangle(10)
