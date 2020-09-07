from funciones import Binomial

# Lanzar 100 veces, prob. de 10 veces cara
prob = Binomial(100, 10)/(2**100)
print("Al lanzar 100 veces, la probabilidad de 10 veces cara es del {}%"
      .format(prob * 100))

# Lanzar 100 veces, prob. más de 30 veces cara
tot_prob = 0
# Se hace un ciclo por ser más de 30 y no solo 30
for i in range(31, 101):
    tot_prob += Binomial(100, i)/(2**100)
print("Al lanzar 100 veces, la probabilidad de más de 30 veces cara es del {}%"
      .format(tot_prob * 100))
