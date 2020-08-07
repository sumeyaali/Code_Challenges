def palindromeRearranging(inputString):
    counter = 0

    # if len(inputString) % 2 != 0:
    #     return False
    
    for char in inputString:
        input_count = inputString.count(char) 
        if len(inputString) % 2 == 0:
            if input_count % 2 != 0:
                return False
        else:
            if input_count == 1:
                counter += 1
    if counter > 1:
        return False
           
    return True