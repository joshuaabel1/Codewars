
def multiplication_table(size):
    tabla = []
    for i in range(1, size+1):
        fila = []
        for j in range(1, size+1):
            fila.append(i * j)
        tabla.append(fila)
    return tabla