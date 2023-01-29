
def exp_sum(n):
    # Crea un diccionario que almacenará los resultados parciales de la función
    results = {}

    # Define una función auxiliar que calculará el número de maneras en que se puede sumar un número
    def exp_sum_helper(n, max_num):
        # Si ya se ha calculado el resultado para este caso, devuélvelo directamente
        if (n, max_num) in results:
            return results[(n, max_num)]

        # Si el número es 0, solo hay una manera de sumarlo (usando el número 0)
        if n == 0:
            return 1

        # Si el número es menor que 0, no hay maneras de sumarlo
        if n < 0:
            return 0

        # Si el máximo número que se puede usar es 0, no hay maneras de sumar el número
        if max_num == 0:
            return 0

        # Inicializa el contador de maneras en 0
        ways = 0

        # Recorre los números desde el máximo hasta 1
        for i in range(max_num, 0, -1):
            # Suma el número de maneras en que se puede sumar el número restando el número actual
            ways += exp_sum_helper(n - i, i)

        # Almacena el resultado en el diccionario
        results[(n, max_num)] = ways

        # Devuelve el resultado
        return ways

    # Llama a la función auxiliar con el número y el máximo número que se puede usar para sumarlo
    return exp_sum_helper(n, n)