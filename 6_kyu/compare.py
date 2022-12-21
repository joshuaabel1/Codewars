def comp(a, b):
    # revisamos que no esten vacias     
    if a == None or b == None:  
        return False
    # primero vamos a recorrer las listas y formar nuestras listas
    list_a = []
    for elemt in a:
        list_a.append(elemt**2)

    if sum(list_a) == sum(b) and sorted(list_a) == sorted(b):
        return True
            
    else:
        return False  