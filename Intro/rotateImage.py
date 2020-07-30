def rotateImage(a):
    n = len(a)
    
    #1. Switch diagnally 
    for i in range(0,n):
        for j in range(i,n):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
            
    for i in range(0,n):
        for j in range(0,n//2):
            temp = a[i][j]
            a[i][j] = a[i][n-1-j]
            a[i][n-1-j] = temp
    return a