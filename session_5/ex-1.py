def count_a(seq):
    """counting the number of As in the sequence"""

    # counter for the As
    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    # return the result
    return result

# main program
s = "AGTACACTGGT"
na = count_a(s)
print("the number of As is: {}".format(na))

# calculate the total length
total = len(s)

#calculate the per of As in the sequence
percen = round(100.0 * na/total, 1)
print("this sequence is {} bases in length".format(total))
print("the percentages of As is {}%".format(percen))