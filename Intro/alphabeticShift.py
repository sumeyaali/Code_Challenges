def alphabeticShift(input):
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    input = list(input)
    
    for i in range(len(input)):
        
        if input[i] == 'z':
            input[i] = 'a'
        else: 
            index = letters.index(input[i])
            input[i] = letters[index + 1]
    
       
    return "".join(input)