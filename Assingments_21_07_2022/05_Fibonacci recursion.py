def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = -1
while n <= 0:
    n = int(input("Enter n(n > 0): "))
print(f'Fib({n}) = {fibonacci(n)}')
