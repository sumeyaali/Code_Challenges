def addBorder(picture):
    output_array = []
    last = (len(picture) -1)
    
    picture.append("*" * (len(picture[0])))
    picture.insert(0, "*" * (len(picture[0])))
    
    for i in range(len(picture)):
        string = list(picture[i])
        string.append("*")
        string.insert(0,"*")
        string_ouput = "".join(string)
        
        output_array.append(string_ouput)

    return output_array