def commonCharacterCount(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    repeating_counter = 0
    
    for i in s1:
        if i in s2:
            repeating_counter += 1
            s2.remove(i)
            
            
        # for j in range(0,len(s2)):   
        #     if s1[i] == s2[j]:
        #         repeating_counter += 1
    return repeating_counter