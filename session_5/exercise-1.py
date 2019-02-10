#counting the number of bases in the sequence
def count_bases(seq):
    dict_of_bases = {}
    # counter for the bases
    bases = ['A', 'C', 'T', 'G']
    for key in bases:
        dict_of_bases[key] = seq.count(key)

    # return the result
    return dict_of_bases


seq = input("enter a sequence")
dict_of_bases = count_bases(seq)
total = len(seq)
print("this sequence is {} bases in lengh".format(len(seq)))
for key in dict_of_bases:
    print("base", key)
    print("count:", dict_of_bases[key])
    if total > 0:
        percen = round(100.0 * dict_of_bases[key]/total, 1)
    else:
        percen = 0
    print("percentage:", percen )




