def high_and_low(numbers):
    list_number = []
    # ...
    for i in numbers.split():
        list_number.append(int(i))
    return f'{max(list_number)} {min(list_number)}'