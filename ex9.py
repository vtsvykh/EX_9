class StrandsDNA:
    all_strands = []

    def __init__(self, strands):
        """
        The function sets attributes for an instance of a class.
        :param strands: the DNA chain
        """
        self.strands = StrandsDNA.all_strands.append(strands)

    @classmethod
    def add_strands(cls, strands):
        """
        The function adds DNA strands.
        :param strands: the DNA chain
        :return: updated list of DNA strands
        """
        list_strands = strands.split()
        StrandsDNA.all_strands.extend(list_strands)

    def get_max_strands(self):
        """
        The function finds a chain of maximum length.
        :return: maximum length string
        """
        max_len = max(len(strand) for strand in StrandsDNA.all_strands)
        max_strand = sorted(set(strand for strand in StrandsDNA.all_strands if max_len == len(strand)))
        return max_strand
