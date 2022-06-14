def pow(m, n):

    # This function will calculate the nth power of a given number

    res = 1
    count = 0
    while count < n:
        res = res * m
        count += 1
    return res


def square(n):
    return n * n


def is_even(n):

    # This function will check is the number even or not

    if n % 2 == 0:
        return True
    else:
        return False


def fast_pow(m, n):

    # Iterative form of fast_pow(m,n) function

    res = 1
    count = 0
    while count < n:
        if is_even(n):
            res = square(pow(m, n/2))
        else:
            res = m * pow(m, n-1)
        count += 1
    return res

# Function call


print(fast_pow(2, 7))
