
import re


def validate_pin(pin):
    
    lists= []
    numbers = '1234567890'
    for i in pin:
        if i not in numbers:
            return False
        else:
            lists.append(i)
            
    if len(lists) == 4 or len(lists) == 6:
        return True
    
    return False