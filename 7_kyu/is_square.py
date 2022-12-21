import math


def is_square(n):    
    if n < 0:
        return False
    
    if n*n == 0:
        return True
    
    result = math.sqrt(n)

    if ((result)**2) == n :
        return True
    
    else:
        return False
    