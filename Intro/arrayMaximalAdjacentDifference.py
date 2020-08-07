def arrayMaximalAdjacentDifference(inputArray):
    # loop through array
    # find max difference at i and j points
    new_array = []
    for i in range(len(inputArray) -1):
        # for j in range(len(inputArray)):
        max_num = abs(inputArray[i] - inputArray[i+1])
        print("max",max_num)
        new_array.append(max_num)
        # print("What is this",max_number)
        
    return max(new_array)
            