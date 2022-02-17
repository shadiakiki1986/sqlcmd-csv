def find_char(s, c):
  return [i for i,x in enumerate(list(s)) if x==c]


def shift_list(l1):
    l2 = l1.copy()
    l2.append(l2.pop(0))
    l2[-1] = None
    return l2


class FixedWidthSplitter:
    """
    Implies edge positions from a sample with commas, then splits strings with those positions.
    Usage:
    sp = FixedWidthSplitter("---,------")
    sp.split("abc,defghi")
    """
    def __init__(self, result_dashes):
        assert result_dashes[0]=='-'
        pos = [0] + find_char(result_dashes, ",") # positions of ,
        self.edges = list(zip(pos, shift_list(pos))) # start/end pairs
        self.pos = pos
    def split(self, res_i):
        o = [res_i[(0 if start==0 else start+1):end].strip() for start,end in self.edges]
        return o
