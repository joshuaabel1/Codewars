def find_it(numbers):
    occurrences = {}
    
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1

    for number, count in occurrences.items():
        if count % 2 == 1:
            return number