
def disemvowel(string_):
    for s in 'aeiouAEIOU':
        string_=string_.replace(s,'')
        
    return string_