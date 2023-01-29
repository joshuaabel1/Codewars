
def is_isogram(string):
    #your code here
    for i in string:
        if string.lower().count(i) > 1:
            return False
    else:
        return True