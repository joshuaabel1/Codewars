def is_valid_walk(walk):
  # Si la longitud de la caminata no es igual a 10, entonces no es válida
    if len(walk) != 10:
        return False

  # Inicializamos las variables que llevarán el recuento de direcciones
    north = 0
    south = 0
    east = 0
    west = 0

  # Recorremos la lista de direcciones y aumentamos el contador de la dirección correspondiente
    for direction in walk:
        if direction == 'n':
            north += 1
        elif direction == 's':
            south += 1
        elif direction == 'e':
            east += 1
        elif direction == 'w':
            west += 1
    
    return north == south and east == west