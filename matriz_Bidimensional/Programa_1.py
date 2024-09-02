# Definir la matriz 3x3
matriz = [
    [20, 30, 50],
    [200, 500, 600],
    [9, 15, 25]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return f"Se encontró el valor {valor_buscado} en la posición ({i}, {j})"
    return f"No se encontró el valor {valor_buscado} en la matriz."

# Definir el valor que quieres buscar
valor_a_buscar = int(input("Ingresa el valor que deseas buscar: "))

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)