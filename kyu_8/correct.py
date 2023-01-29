
def correct(s):
    dict = {'0':'O','5':'S','1':'I'}
    result = ''
    for i in s:
        if i in dict:
            result += dict[i]
        else:
            result += i
            
    return result 
        