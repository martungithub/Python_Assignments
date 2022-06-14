def fib_iter(n):
    # a = F(0) = 0
    a = 0
    # b = F(1) = 1
    b = 1
    # c = F(2) = 2
    c = 2
    # if n < 3 F(n) = n so return n
    if n < 3:
        return n
    # if n >= 3 F(n) = F(n - 1) + F(n - 2) + F(n - 3)
    while n >= 3:
        a, b = b, a
        b, c = c, b
        c = a + b + c
        n -= 1
    return c

# Function call
print(fib_iter(6))

