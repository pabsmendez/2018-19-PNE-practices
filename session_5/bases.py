def count_bases(seq):
    dict_of_bases = {}
    # counter for the bases
    bases = ['A', 'C', 'T', 'G']
    for key in bases:
        dict_of_bases[key] = seq.count(key)

    # return the result
    return dict_of_bases