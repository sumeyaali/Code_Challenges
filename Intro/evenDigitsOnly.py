def evenDigitsOnly(n):
    
    n = str(n)
    print(n)
    for num in n:      
        print(num)
        if int(num) % 2 != 0:
            return False
    return True
