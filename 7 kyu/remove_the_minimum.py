def remove_smallest(numbers):
    # Vemos que la lista numbers no este vacia.
    if len(numbers) == 0:
        return []
    # Declaramos una lista vacia, donde ira nuestro resultado.
    lists = []
    for i in numbers:
        lists.append(i)
    min_number = min(lists)
    result = lists.index(min_number)
    lists.pop(result)
    resp = lists
    return resp