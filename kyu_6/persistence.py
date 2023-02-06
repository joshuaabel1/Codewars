
def persistence(num):
    count = 0
    while num >= 10:
        digits = [int(x) for x in str(num)]
        result = 1
        for d in digits:
            result *= d
        num = result
        count += 1
    return count