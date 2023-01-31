
def number(bus_stops):
    start = 0
    for i in bus_stops:
        start += i[0] - i[1]
    return start