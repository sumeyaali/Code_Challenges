def firstDuplicate(a):
    
    my_dict = {}
    for i in range(len(a)):
        # duplicate = 0 
        if a[i] not in my_dict:
            my_dict[a[i]] = 0
        elif a[i] in my_dict:
            return a[i]
       
    return -1
