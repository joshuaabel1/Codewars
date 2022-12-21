def points(games):
    our_points =  0
    for i in games:
        comp = i.split(':')
        if int(comp[0]) > int(comp[1]):
            our_points += 3

        elif int(comp[0]) == int(comp[1]):
            our_points += 1

    return our_points