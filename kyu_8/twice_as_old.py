
def twice_as_old(dad_years_old, son_years_old):
    diff = dad_years_old - (2 * son_years_old)
    if diff >= 0:
        return diff
    else:
        return abs(diff)