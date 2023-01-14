def sum_array(arr):
    # Primero vemos que sea diferente a None
    if arr == None:
        return 0
    # Nos aseguramos que el contenido de la lista sea mayor a 1
    if len(arr) > 1 :
        max2 = max(arr)
        result_max = arr.index(max2)
        arr.pop(result_max)
        min2 = min(arr)
        result_min = arr.index(min2)
        arr.pop(result_min)

        return sum(arr)
    # Por defecto retornamos 0
    return 0