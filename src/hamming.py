class Hamming:
    """
    >>> hamming = Hamming()
    >>> hamming.distance('','')
    0
    >>> hamming.distance('A', '')
    Traceback (most recent call last):
    ...
    ValueError: Values cannot be of different length
    >>> hamming.distance('', 'A')
    Traceback (most recent call last):
    ...
    ValueError: Values cannot be of different length
    >>> hamming.distance("A", "A")
    0
    >>> hamming.distance('A', 'B')
    1
    >>> hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
    0
    >>> hamming.distance("GGACGGATTCTG", "AGGACGGATTCT")
    9
    >>> hamming.distance('a', 'A')
    1
    >>> hamming.distance('AATG','AAA')
    Traceback (most recent call last):
      ...
    ValueError: Values cannot be of different length
    >>> hamming.distance('AGT', 'GGTA')
    Traceback (most recent call last):
      ...
    ValueError: Values cannot be of different length
    """
    def distance(self, first, second):
        if len(first) != len(second):
            raise ValueError('Values cannot be of different length')
        counter = 0
        for i in range(0, len(first)):
            if first[i] != second[i]:
                counter += 1
        return counter
