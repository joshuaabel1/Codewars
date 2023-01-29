
def gimme(input_array):
    # Implement this function
    min_value = min(input_array)
    max_value = max(input_array)
    result = 0
    for i in input_array:
        if i > min_value and i < max_value:
            result = input_array.index(i)
    return result