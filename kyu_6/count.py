
def count(string):
    # The function code should be here
    if len(string) == 0:
        return {}
        
    return {x:string.count(x) for x in string}