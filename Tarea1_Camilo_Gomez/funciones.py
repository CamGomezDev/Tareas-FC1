def Factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i

    return fact


def Binomial(n, k):
    numerator = Factorial(n)
    denominator = Factorial(k)*Factorial(n-k)

    return numerator/denominator


def Pascal(n):
    digits = len(str(int(Binomial(n, int(n/2)))))
    for i in range(n+1):
        row = int(((n-i)/2)*(digits+1))*" "
        for k in range(i+1):
            coef = int(Binomial(i, k))
            spaces_n = digits + 1 - len(str(coef))
            spaces_left = int(spaces_n/2)
            spaces_right = int(spaces_n/2) + spaces_n % 2
            row += spaces_left*" "
            row += "{}".format(coef)
            row += spaces_right*" "
        print(row)


Pascal(14)
                               