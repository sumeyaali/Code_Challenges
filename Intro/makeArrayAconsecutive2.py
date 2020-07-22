def makeArrayConsecutive2(statues):
    min_num = min(statues)
    max_num = max(statues)
    # nums in range lets you know how many nums are between min and max
    num_in_range = (max_num + 1 ) - min_num
       
    return num_in_range - len(statues)
