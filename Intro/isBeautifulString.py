from collections import Counter

def isBeautifulString(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1,len(a)): 
        if s.count(a[i-1]) >= s.count(a[i]):
            continue
        return False
    return True