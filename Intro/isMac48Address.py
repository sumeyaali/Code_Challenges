def isMAC48Address(inputString):
    letters = ['A','B', 'C','D','E','F']
    string = inputString.split('-')
    input = len(string)

    if input != 6:
        return False
    for i in range(input):
        subInput = string[i]
        subString = len(subInput)
        if subString != 2:
            return False
        for j in range(subString): 
            if ((subInput[j].isnumeric() == False) and  (subInput[j] not in letters)):
                return False
    return True