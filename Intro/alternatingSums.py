def alternatingSums(a):
    team1_sum = []
    team2_sum = []
    output_array = []
    
    for i in range(len(a)):
        if i % 2 == 0:
            team1_sum.append(a[i])
        else:
            team2_sum.append(a[i])
    output_array = sum(team1_sum), sum(team2_sum)
    
    return output_array