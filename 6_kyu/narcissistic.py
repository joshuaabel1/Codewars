def narcissistic(value):
    # Code away
    x = [int(a) for a in str(value)]
    potencia = len(x)
    result = []
    for i in x:
        parse_num = i**int(potencia)
        result.append(parse_num)
    if sum(result) == value:
        return True
    else:
        return False