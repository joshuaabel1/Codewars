
def accum(s):
    count = 0  
    result = []
    for i in s:
        count += 1
        parse = i * count
        result.append(parse.capitalize())
    
    return '-'.join(result)