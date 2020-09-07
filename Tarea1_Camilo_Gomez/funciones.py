def Factorial(n: int):
    """Calcula el factorial de un número"""
    fact = 1
    # Ciclo de factorial
    for i in range(n, 0, -1):
        fact *= i

    return int(fact)


def Binomial(n: int, k: int):
    """Calcula el coeficiente binomial usando la función factorial"""
    numerator = Factorial(n)
    denominator = Factorial(k)*Factorial(n-k)

    res = numerator/denominator

    return int(res)


def Pascal(n: int):
    """Genera un archivo con un triángulo de Pascal de n+1 filas"""
    # Calcula el número de dígitos del valor más grande del triángulo
    digits = len(str(int(Binomial(n, int(n/2)))))
    f = open("Pascal-{}.txt".format(n), "w+")
    # Ciclo sobre las filas
    for i in range(n+1):
        # Cantidad de espacios al principio del triángulo
        row = int(((n-i)/2)*(digits+1))*" "
        # Ciclo sobre cada coeficiente en la fila
        for k in range(i+1):
            # Cálculo del coeficiente
            coef = int(Binomial(i, k))
            # Cantidad de espacios a la derecha e izquierda (esto es lo que
            # permite espacios dinámicos)
            spaces_n = digits + 1 - len(str(coef))
            spaces_left = int(spaces_n/2)
            spaces_right = int(spaces_n/2) + spaces_n % 2
            row += spaces_left*" "
            row += "{}".format(coef)
            row += spaces_right*" "
        # Escribe la fila en el archivo
        f.write("{}\n".format(row))

    f.close()
