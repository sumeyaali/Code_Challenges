 def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 0
    # what we gain every day
    height = 0
    # print(height)
    # how many days does it take to reach desiredHeight

    while height < desiredHeight:
        print(height)
        height += upSpeed 
        if height < desiredHeight:
            height -= downSpeed
        days += 1  
        # print(days)
    return days

# day 1: 6-5 -> 1
# day 2: 7-5 -> 2
# day 3: 8-5 -> 3
# day 4 :9-5 -> 4
# day 5: 10-5 -> 5