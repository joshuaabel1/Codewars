
def find_uniq(arr):
    
    min_value = min(arr)
    max_value = max(arr)
    if arr.count(min_value) > 1:
        return max_value
    
    return min_value