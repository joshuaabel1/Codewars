def printer_error(s):
    # your code
    errors = 0
    colours = len(s)
    colours_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for i in s:
        if i not in colours_list:
            errors += 1

    return f"{errors}/{colours}"