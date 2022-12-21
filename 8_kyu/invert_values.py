def invert(lst):
    reverse_lst = []
    for i in lst:
        reverse_lst.append(i-i*2)
        
    return reverse_lst