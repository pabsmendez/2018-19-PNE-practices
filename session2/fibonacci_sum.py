def fibonacci(n):
    d = 0
    c = 1
    countf = 0
    for i in range(n+1):
        countf += d
        d, c = c, (d+c)
    print(countf)
    return
fibonacci(int(input("fibonacci number")))
