def dig_pow(n, p):
    # Función auxiliar para obtener la lista de dígitos de un número entero.
    def digits(n):
        return [int(d) for d in str(n)]
    
    # Obtenemos la lista de dígitos de n.
    digits = digits(n)
    
    # Calculamos la suma de cada dígito elevado a la potencia indicada.
    sum = 0
    for i, d in enumerate(digits):
        sum += d ** (p + i)
    
    # Si la suma es múltiplo de n, devolvemos el cociente. Si no, devolvemos -1.
    return sum // n if sum % n == 0 else -1