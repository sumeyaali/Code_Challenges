def arrayChange(inputArray):
    # loop through the inout array:
    
    # sum= i - j + 1
    count = 0
    # J = j + sum
    
    for i in range(len(inputArray) -1):
        if inputArray[i] >= inputArray[i + 1]:
            sum = inputArray[i] - inputArray[i + 1] + 1
            count += sum
            inputArray[i + 1] = inputArray[i+1] + sum
    return count
