def absoluteValuesSumMinimization(a):
    sums_array = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += abs(a[i]- a[j])
        sums_array.append(sum)
    # find min of the sums array
    min_num = min(sums_array)
    # find index of min 
    index_list = sums_array.index(min_num)

    # return corresponding index of a 
    return a[index_list]