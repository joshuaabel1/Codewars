
def find_short(s):
    # your code here
    l = 0
    result = []
    for i in s.split(" "):
        result.append(len(i))
        
    return min(result) # l: shortest word length