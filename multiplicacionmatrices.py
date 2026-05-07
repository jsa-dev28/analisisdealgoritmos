import random
import time
import matplotlib.pyplot as plt

# Multiplicación clásica de matrices.
# Tiene 3 bucles anidados.
# Cantidad de operaciones:
# Aproximadamente n³
# Complejidad: O(n³)

def multiplicar_matrices(A, B):
    n = len(A)
    resultado = []
    for i in range(n):
        fila = []
        for j in range(n):
            suma = 0
            for k in range(n):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

# TEST 

valores = [5, 10, 20, 30, 40]
tiempos = []

for n in valores:

    A = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]
    inicio = time.time()
    multiplicar_matrices(A, B)
    fin = time.time()
    tiempos.append(fin - inicio)

# GRAFICO

plt.plot(valores, tiempos)

plt.xlabel("Dimension de la matriz")
plt.ylabel("Tiempo")
plt.title("Multiplicacion de matrices")

plt.grid()

plt.show()