    if sorted(a) != sorted(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    if counter > 2:
        return False
    return True