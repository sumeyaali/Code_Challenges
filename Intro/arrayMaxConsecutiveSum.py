def arrayMaxConsecutiveSum(array, k):
    # iterate through the input Array 
    # k_sum is the sum of the first two numbers added together
    k_sum = sum(array[0:k])
    max_sum = k_sum
    for i in range(k,len(array)):
        k_sum = k_sum - array[i-k] + array[i]
        if k_sum > max_sum:
            max_sum = k_sum    
    return max_sum