from bases import count_bases
sequence1 = input("first sequence")
sequence2 = input("second sequence")
sequences = sequence1, sequence2
nsequences = 0
for b in sequences:
    dict_of_bases = count_bases(b)
    nsequences += 1

    total = len(b)
    print("the sequence {} is {} bases in lengh".format(nsequences,len(b)))
    for key in dict_of_bases:
        print("base", key)
        print("count:", dict_of_bases[key])
        if total > 0:
            percen = round(100.0 * dict_of_bases[key]/total, 1)
        else:
            percen = 0
        print("percentage:", percen)