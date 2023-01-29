
def fake_bin(x):
    number_str = ''
    for i in x:
        if int(i) < 5:
            number_str += i.replace(i, '0')
        else:
            if int(i) >= 5:
                number_str += i.replace(i, '1')
    return number_str