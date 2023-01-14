def filter_list(l):
    'return a new list with the strings filtered out'
    list_int = []
    for i in l:
        if type(i) is int:
            list_int.append(i)
    return list_int