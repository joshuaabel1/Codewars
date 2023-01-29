
def abbrev_name(name):
    list_name = name.split()
    result = f'{list_name[0][0].upper()}.{list_name[1][0].upper()}'
    return result