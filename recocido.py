import random
import math

# Función de energía
def energy(x):
    return x**2

# Variables iniciales
TempIni = 100
TempMin = 1e-3
alpha = 0.9
x = random.uniform(-10, 10)
E_best = energy(x)

# Bucle principal
while TempIni > TempMin:
    x_new = random.uniform(x-1, x+1)
    E_new = energy(x_new)
    delta_E = E_new - energy(x)
    if delta_E < 0:
        x = x_new
        E = E_new
        if E_new < E_best:
            x_best = x_new
            E_best = E_new
    else:
        p = math.exp(-delta_E / TempIni)
        if random.uniform(0, 1) < p:
            x = x_new
            E = E_new
    TempIni *= alpha

# Resultados
print("Solución óptima: x =", x_best)
print("Valor de energía: E =", E_best)