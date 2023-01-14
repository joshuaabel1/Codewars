def solution(s):
    if len(s)/2 != 0:
        s = s+'_'
    
    lists = []
    x = [a for a in s]
    parser = ''
    for i in x:
        parser += i
        if len(parser) == 2:
            lists.append(parser)
            parser = ''

    return lists