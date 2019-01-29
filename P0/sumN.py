def sum(n):
    total = 0
    for n in range(1, 1+n):
        total += n
    return(total)


number = int(input("n = "))
print("the result of the sume of the integer numbers from 1 to n = ")
print(sum(number))
