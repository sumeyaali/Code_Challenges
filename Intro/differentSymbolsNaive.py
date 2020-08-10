from collections import Counter
def differentSymbolsNaive(s):
    counter = Counter(s)
    return len(counter)