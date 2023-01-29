
def to_alternating_case(string):
    result = []
    for char in list(string):
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)