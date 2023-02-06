
def dig_pow(n, p):
    # Funci�n auxiliar para obtener la lista de d�gitos de un n�mero entero.
    def digits(n):
        return [int(d) for d in str(n)]
    
    # Obtenemos la lista de d�gitos de n.
    digits = digits(n)
    
    # Calculamos la suma de cada d�gito elevado a la potencia indicada.
    sum = 0
    for i, d in enumerate(digits):
        sum += d ** (p + i)
    
    # Si la suma es m�ltiplo de n, devolvemos el cociente. Si no, devolvemos -1.
    return sum // n if sum % n == 0 else -1