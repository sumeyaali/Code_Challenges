def isIPv4Address(inputString):
    b = inputString.split('.')
    # print(b)
    # print(inputString.split('.'))
    # list_input = list(inputString)
    # print(list_input)
    if len(b) != 4:
        return False
    for i in range(len(b)):
        # new_list = list(inputString)
        if b[i].isnumeric() == False or b[i] == "":
            return False
        # print(b)
        if int(b[i]) < 10 and len(b[i]) > 1:
            return False
        if int(b[i]) < 0 or int(b[i]) > 255:
            return False
        # else:
        #     return True
    return True