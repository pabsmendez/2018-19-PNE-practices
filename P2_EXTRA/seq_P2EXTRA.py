class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("new sequence created")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        dictofbases = {"A":"T", "T":"A", "C":"G", "G":"C"}
        translation = self.strbases.maketrans(dictofbases)
        strbases_comp = self.strbases.translate(translation)
        return Seq(strbases_comp)

    def reversed(self):
        strbases_revers = self.strbases[::-1]
        return Seq(strbases_revers)

    def count(self, base):
        num_of_bases = self.strbases.count(base)
        return num_of_bases

    def percentage(self, base):
        total = len(self.strbases)
        if total > 0:
            numberbases = self.strbases.count(base)
            percentage = round(100.0 * numberbases/total, 1)
        else:
            percentage = 0
        return percentage