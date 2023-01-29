
def exp_sum(n):
    # Crea un diccionario que almacenar� los resultados parciales de la funci�n
    results = {}

    # Define una funci�n auxiliar que calcular� el n�mero de maneras en que se puede sumar un n�mero
    def exp_sum_helper(n, max_num):
        # Si ya se ha calculado el resultado para este caso, devu�lvelo directamente
        if (n, max_num) in results:
            return results[(n, max_num)]

        # Si el n�mero es 0, solo hay una manera de sumarlo (usando el n�mero 0)
        if n == 0:
            return 1

        # Si el n�mero es menor que 0, no hay maneras de sumarlo
        if n < 0:
            return 0

        # Si el m�ximo n�mero que se puede usar es 0, no hay maneras de sumar el n�mero
        if max_num == 0:
            return 0

        # Inicializa el contador de maneras en 0
        ways = 0

        # Recorre los n�meros desde el m�ximo hasta 1
        for i in range(max_num, 0, -1):
            # Suma el n�mero de maneras en que se puede sumar el n�mero restando el n�mero actual
            ways += exp_sum_helper(n - i, i)

        # Almacena el resultado en el diccionario
        results[(n, max_num)] = ways

        # Devuelve el resultado
        return ways

    # Llama a la funci�n auxiliar con el n�mero y el m�ximo n�mero que se puede usar para sumarlo
    return exp_sum_helper(n, n)