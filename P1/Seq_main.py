from seq import Seq

s1 = Seq(input("first sequence: "))
s2 = Seq(input("second sequence: "))
s3 = Seq.complement(s1)
s4 = Seq.reversed(s3)
bases = "A", "C", "T", "G"
sequences = s1, s2, s3, s4
nsequences = 0
for b in sequences:
    nsequences += 1
    print("sequence{}: {}".format(nsequences, b.strbases))
    print("length: {}".format(b.len()))

    print("count bases:", end=" ")
    for base in bases:
        print("{}: {}".format(base, b.strbases.count(base)),end=" ")
    print()
    print("bases percentage: ", end=" ")
    for base in bases:
        print("{}: {}%".format(base, b.percentage(base)),end=" ")
    print()