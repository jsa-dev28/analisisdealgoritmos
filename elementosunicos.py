import random
import time
import matplotlib.pyplot as plt

# Compara cada elemento con todos los demás.
# Cantidad de operaciones:
# Aproximadamente n²
# Complejidad: O(n²)

def elementos_unicos(lista):

    for i in range(len(lista)):           # n
        for j in range(i + 1, len(lista)):  # n
            if lista[i] == lista[j]:
                return False
    return True

# TEST 

valores = [100, 300, 500, 700, 1000]

tiempos = []

for n in valores:
    lista = [random.randint(1, n*2) for _ in range(n)]
    inicio = time.time()
    elementos_unicos(lista)
    fin = time.time()
    tiempos.append(fin - inicio)


# GRAFICO

plt.plot(valores, tiempos)

plt.xlabel("Tamaño de n")
plt.ylabel("Tiempo")
plt.title("Elementos únicos - Brute Force")

plt.grid()

plt.show()