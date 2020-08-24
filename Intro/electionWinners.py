def electionsWinners(votes, k):
    counter = 0
    max_vote = max(votes)
    
    if k == 0:
        if votes.count(max_vote) == 1:
            return 1
        else:
            return 0  
    for i in range(len(votes)):
        if votes[i] + k > max_vote:
            counter += 1
  
    return counter