def sortByHeight(a):

    num_list = []
    trees_list = []
    
    
    for i in range(len(a)):
        if a[i] != -1:
            num_list.append(a[i])
        else:
            trees_list.append(i)
    num_list.sort()
    for i in trees_list:
        num_list.insert(i, -1)
    # print(trees_list)
    return num_list
            