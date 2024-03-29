class StrandsDNA:
    all_strands = []

    @classmethod
    def add_strands(cls, strands):
        list_strands = strands.split()
        StrandsDNA.all_strands.extend(list_strands)

    def get_max_strands(self):
        max_len = max(len(strand) for strand in StrandsDNA.all_strands)
        max_strand = sorted(set(strand for strand in StrandsDNA.all_strands if max_len == len(strand)))
        return max_strand
