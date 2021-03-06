class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("new sequence created")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """this class is derived from the Seq class
        All the objects of class Gene will inheritance
        the methods from Seq class"""
    pass

s1 = Gene("ATTCGATCC")
s2 = Seq("AAAGG")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("sequence1: {}".format(str1))
print("   length: {}".format(l1))
print("sequence2: {}".format(str2))
print("   length: {}".format(l2))

print("the end")