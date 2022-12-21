def london_city_hacker(journey): 
    # your code here
    metro = 2.40
    bus = 1.50
    total_cost = 0.00
    count = 0
    for i in journey:
        if type(i) is str:
            total_cost += metro
            count = 0
        else:
            if count == 0:
                total_cost += bus
                count += 1
            else:
                count = 0
    return '£{:.2f}'.format(total_cost)