def knapsackLight(value1, weight1, value2, weight2, maxW):
    # if weight1 and weight2 <= maxW:
    # we can carry both
    # if we can't take both, check to see which one has a greater value
    # return the greater value
    
    if weight1 + weight2 <= maxW:
        return value1 + value2
    # if weight1 > maxW and weight2 > maxW:
    #     return 0
    elif weight1 <= maxW and weight2 <= maxW :
        return max(value1, value2)
    elif weight1 <= maxW:
        return value1
    elif weight2 <= maxW:
        return value2
    else:
        return 0