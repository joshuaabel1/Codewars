
def count_sheep(n):
    str_default = "sheep..."
    result = ''
    # your code
    for i in range(1, n + 1):
        result += f"{i} {str_default}"
        
    return result
        
        