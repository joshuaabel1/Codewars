def tribonacci(signature, n):
    # Si n es menor que 3, solo devolvemos los primeros n elementos de la firma
    if n < 3:
        return signature[:n]
    
    # Creamos una lista para almacenar los elementos de la secuencia
    tribonacci_sequence = signature[:]
    
    # Calculamos los elementos restantes de la secuencia
    for i in range(3, n):
        tribonacci_sequence.append(tribonacci_sequence[i-1] + tribonacci_sequence[i-2] + tribonacci_sequence[i-3])
    
    return tribonacci_sequence