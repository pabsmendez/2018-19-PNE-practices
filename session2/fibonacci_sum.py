def fibonacci(n):
    d = int(input())
    c = 1
    while c < n:
        print(c, end = ',')
        c, d = d, c+d
    print()
number = int(input("fibonacci number"))
fibonacci(number)
