def allLongestStrings(inputArray):
    longest_strings = []
    max_length = len(max(inputArray, key = len))
    print(max_length)
    
    
    for i in range(len(inputArray)):
        if len(inputArray[i]) == max_length:
            # print('hello',max_length)
            longest_strings.append(inputArray[i])
        
    return longest_strings