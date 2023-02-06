
def solution(string):
    result = ""
    for c in string:
        if c.isupper(): 
            result += " "
        result += c
    return result