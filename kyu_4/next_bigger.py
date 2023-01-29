
def next_bigger(num):
    digits = [int(d) for d in str(num)]

    for i in range(len(digits)-1, 0, -1):
        if digits[i-1] < digits[i]:
            break
    else:
        return -1

    for j in range(len(digits)-1, i-1, -1):
        if digits[j] > digits[i-1]:
            break

    digits[i-1], digits[j] = digits[j], digits[i-1]

    digits[i:] = sorted(digits[i:])

    return int(''.join(map(str, digits)))