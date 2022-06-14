def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def double(n):
    return n + n


def halve(n):
    return int(n / 2)


def fast_mul(m, n):
    if n == 0:
        return 0
    if is_even(n):
        return fast_mul(double(m), halve(n))
    else:
        return m + fast_mul(m, n - 1)


print(fast_mul(5, 7))
