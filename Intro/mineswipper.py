def minesweeper(matrix):
    output_arr = []
    for i in range(len(matrix)):
        output_arr.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]
            output_arr[i].append(l)
    return output_arr
    