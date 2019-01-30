f = open("Gene.txt")
sequence = f.read()
A = 0
C = 0
G = 0
T = 0
i = 0
print(len(sequence))
while i < len(sequence):
    base = sequence[i]
    if base == ">" :
        i += (sequence[i:].find("\n"))
    elif base == "A":
        A += 1
        i += 1
    elif base == "C":
        C += 1
        i += 1
    elif base == "G":
        G += 1
        i += 1
    elif base == "T":
        T += 1
        i += 1
    else:
        i += 1
print("A:", A, "C:", C, "G:", G, "T:", T)