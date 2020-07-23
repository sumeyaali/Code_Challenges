def matrixElementsSum(matrix):
    sum = 0
    bannedIndex = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                bannedIndex.append(j)
            elif j not in bannedIndex:
                sum += matrix[i][j]
    return sum