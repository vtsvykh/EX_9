class StrandsDNA:
    """
    Class of Strands DNA.
    """
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
        StrandsDNA.all_strands.append(list_strands)

    def get_max_strands(self):
        """
        The function finds a chain of maximum length.
        :return: maximum length string
        """
        new_list = sum(StrandsDNA.all_strands, [])
        max_len = max(len(strand) for strand in l)
        max_strand = sorted(set(strand for strand in l if max_len == len(strand)))
        for elem in max_strand:
            for item in range(len(StrandsDNA.all_strands)):
                if elem in StrandsDNA.all_strands[item]:
                    print(StrandsDNA.all_strands[item])
