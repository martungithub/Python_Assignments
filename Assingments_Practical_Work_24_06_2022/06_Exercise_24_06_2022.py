def is_prime(n):
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True


def smallest_prime(n):
    n = n + 1
    while not is_prime(n):
        n = n + 1
    return n


print(smallest_prime(47))
