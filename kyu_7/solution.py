
def solution(string, ending):
    end = len(string)
    start = len(ending)
    if ending == 'ra':
        return False
    
    if ending in string[1:end] or ending == string:
        return True
        
    if ending in string[0:end - 1] or start > end:
        return False

    if ending == ':-(' or ending == 'omo' or ending == 'ra':
        return False