def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        print(fib)
    return fib[n]

print(fibonacci_bottom_up(5))  # Çıktı: 55
