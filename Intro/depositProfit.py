def depositProfit(deposit, rate, threshold):
    rate = rate/100
    years = 0
    while deposit < threshold:
        deposit += deposit * rate
        years += 1
    return years
