def fibonacci(n):
    c, d = 2, 4
    while c < n:
        print(c, end = ',')
        c, d = d, c+d
    print()
fibonacci(7)
