def digital_root(n):
    lists=[]
    result = 0
    for i in str(n):
        lists.append(int(i))
        result = sum(lists)

    while result > 9:
        new_numbers = sum(lists)
        lists=[]
        for i in str(new_numbers):
            lists.append(int(i))
            result = sum(lists)
    return result