from funciones import Factorial, Binomial, Pascal
import numpy as np
import filecmp

# Test Factorial
if Factorial(0) == 1 and Factorial(1) == 1 and \
      Factorial(2) == 2 and Factorial(3) == 6 and \
      Factorial(4) == 24 and Factorial(5) == 120 and \
      Factorial(6) == 720 and Factorial(7) == 5040 and \
      Factorial(8) == 40320:
    print("Prueba de factorial pasada exitosamente")

if Binomial(10, 5) == 252 and Binomial(9, 6) == 84 and \
      Binomial(8, 7) == 8 and  \
      Binomial(np.random.randint(low=1, high=100), 0) == 1:
    print("Prueba del coeficiente binomial pasada exitosamente")

Pascal(14)
Pascal(19)
if filecmp.cmp("Pascal-14-test.txt", "Pascal-14.txt") and \
      filecmp.cmp("Pascal-19-test.txt", "Pascal-19.txt"):
    print("Prueba del triángulo de Pascal pasada exitosamente")