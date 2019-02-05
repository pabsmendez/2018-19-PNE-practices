sequence = input("enter a new sequence:")
print("total length", len(sequence))
A = 0
C = 0
G = 0
T = 0
for letter in sequence.lower():
    if letter is "a":
        A += 1
    elif letter is "c":
        C += 1
    elif letter is "g":
        G += 1
    elif letter is "t":
        T += 1
print("A:", A)
print("C:", C)
print("G:", G)
print("T:", T)
