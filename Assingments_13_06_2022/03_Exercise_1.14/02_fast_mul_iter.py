def double(n):

    # This function will multiply the number by 2. We do not have * oper

    return n + n


def smallest_of_two_numbers(a, b):
    if a >= b:
        return a
    else:
        return b


def greatest_of_two_numbers(a, b):
    if a <= b:
        return a
    else:
        return b


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def halve(n):
    return int(n / 2)


def fast_mul(a, b):
    mul = 0
    count = 0
    if is_even(a) and not is_even(b):
        count = halve(a)
    elif is_even(b) and not is_even(a):
        count = halve(b)
    elif not is_even(a) and not is_even(b) or is_even(a) and is_even(b):

        count = smallest_of_two_numbers(a, b)

    while count != 0:
        if is_even(a) and not is_even(b):
            mul += double(b)
        elif is_even(b) and not is_even(a):
            mul += double(a)
        elif is_even(a) and is_even(b):
            mul += halve(smallest_of_two_numbers(a, b)) + greatest_of_two_numbers(a, b)
        elif not is_even(a) and not is_even(b):
            mul += greatest_of_two_numbers(a, b)
        else:
            mul += a
        count -= 1
    return mul


print(fast_mul(4, 4))
