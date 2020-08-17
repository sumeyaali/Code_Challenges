def longestDigitsPrefix(inputString):
    # iterate through the string
    arr = ''
    for i in inputString:
        if i.isdigit():
            arr += i
        else:
            break
    return arr