from bases import count_bases
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