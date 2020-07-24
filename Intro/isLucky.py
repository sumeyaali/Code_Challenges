def isLucky(n):
    n = str(n)
    print(n)
    mid_length = int(len(n) / 2)
    left = n[:mid_length]
    print("Left",left)
    right = n[mid_length:]
    print("right", right)
    
    total_right = 0
    total_left = 0
    for i in right:
        total_right += int(i)
    for i in left:
        total_left += int(i)
        
    if total_left == total_right:   
        return True
    return False