# Definir la matriz 3x3
matriz = [
    [500, 30, 10],
    [2000, 900, 600],
    [9, 25, 15]
]

# Función para ordenar una fila usando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para ordenar cada fila de la matriz
def ordenar_matriz(matriz):
    for fila in matriz:
        bubble_sort(fila)

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la matriz
ordenar_matriz(matriz)

# Mostrar la matriz ordenada
print("\nMatriz ordenada:")
for fila in matriz:
    print(fila)