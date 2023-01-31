
def number(lines):
    #your code here
    count = 1
    result = []
    for i in lines:
        line = f"{count}: {i}"
        result.append(line)
        count += 1
        
    return result