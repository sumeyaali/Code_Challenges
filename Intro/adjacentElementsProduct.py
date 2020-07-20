def adjacentElementsProduct(inputArray):
    # my_dict = {}
    
    # for i in range(len(inputArray) -1):
    #     my_dict[inputArray[i] * inputArray[i+1]] = 0    
    # return max(my_dict)
    max_num = -1000
    
    for i in range(len(inputArray) -1):
        if inputArray[i] * inputArray[i + 1] > max_num:
            max_num = inputArray[i] * inputArray[i + 1]
    return max_num