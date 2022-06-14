def f(n, a=0, b=1, c=2):
    if n < 3:
        return n
    return f(n - 1, a) + f(n - 2, b) + f(n - 3, a + b + c)
print(f(4))