def boxBlur(image):
    
    output_arr = []
    # row
    for i in range(len(image) - 2):
        temp_arr = []
        # column
        for j in range(len(image[i]) - 2):
            sum = 0
            # row 3x3
            for a in range(i, i+3):
                # column 3x3
                for b in range(j, j+3):
                    sum += image[a][b]
            temp_arr.append(sum//9)
        output_arr.append(temp_arr)
    return output_arr
