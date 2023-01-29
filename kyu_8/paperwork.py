
def paperwork(n, m):
    if (n or m) < 0 or (n or m) == 0:
        return 0

    elif (n and m) < 0:
        return 0
    else:
        return n * m