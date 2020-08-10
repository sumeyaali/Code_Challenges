def extractEachKth(inputArray, k):
    # deleting kth index -1 and for every kth number (whatever k is)
    del inputArray[k-1::k]
    return inputArray