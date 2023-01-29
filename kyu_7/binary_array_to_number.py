
def binary_array_to_number(arr):
    result = 0
    for i, digit in enumerate(reversed(arr)):
        if digit == 1:
            result +=2**i
    
    return result