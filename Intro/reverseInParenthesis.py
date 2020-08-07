def reverseInParentheses(inputString):
    char = list(inputString)
    new_string = ""
    stack = []
    for i in range(len(char)):
        if char[i] == "(":
            stack.append(i)
        elif char[i] == ")":
            j = stack.pop()
            char[j:i] = char[i:j:-1]
    for i in range (len(char)):
        if char[i] != ")":
            new_string += char[i]
        
    return new_string