import random
import time
import matplotlib.pyplot as plt

# BUSQUEDA LINEAL
# Recorre elemento por elemento hasta encontrar el valor.
# Cantidad de operaciones aproximadas:
# Mejor caso: 1
# Peor caso: n
# Complejidad: O(n)

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):   # n operaciones
        if lista[i] == objetivo:  # comparación
            return i
    return -1


# BUSQUEDA BINARIA
# Solo funciona con listas ordenadas.
# En cada paso divide el problema a la mitad.
# Cantidad de operaciones aproximadas:
# log2(n)
# Complejidad: O(log n)

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio

        elif lista[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1


# TEST DE TIEMPOS 

valores = [100, 1000, 5000, 10000, 20000]

tiempos_lineal = []
tiempos_binaria = []

for n in valores:

    lista = list(range(n))
    objetivo = n - 1

    # LINEAL
    inicio = time.time()
    busqueda_lineal(lista, objetivo)
    fin = time.time()

    tiempos_lineal.append(fin - inicio)

    # BINARIA
    inicio = time.time()
    busqueda_binaria(lista, objetivo)
    fin = time.time()

    tiempos_binaria.append(fin - inicio)


# GRAFICO

plt.plot(valores, tiempos_lineal, label="Lineal")
plt.plot(valores, tiempos_binaria, label="Binaria")

plt.xlabel("Tamaño de n")
plt.ylabel("Tiempo")
plt.title("Busqueda lineal vs binaria")

plt.legend()
plt.grid()

plt.show()