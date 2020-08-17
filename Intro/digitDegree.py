def digitDegree(n):
    count = 0
    while True:
        if n >= 10: 
            # for i in str(n):
            n = sum([int(i) for i in str(n)])
            count += 1
        else:
            return count