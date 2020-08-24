def avoidObstacles(inputArray):
    # loop through inputArray
    inputArray= sorted(inputArray)
    print(inputArray)
    
    jump = 1
    
    obstacle = True
    
        
    
    while obstacle: 
        obstacle = False
        jump += 1 
        
        for i in range(len(inputArray)):
            if inputArray[i] % jump == 0:
                obstacle = True
                break
    return jump