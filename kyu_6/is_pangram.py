
def is_pangram(s):
    a_z = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    for i in s:
        if i.lower() in a_z:
            result += i
    for i in a_z:
        if i not in result.lower():
            return False
    
    return True