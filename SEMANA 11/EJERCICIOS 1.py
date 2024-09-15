def buscar_en_matriz(matriz, valor):
    # Recorremos la matriz para buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición si se encuentra el valor
    return None  # Devuelve None si no se encuentra el valor

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Solicitamos al usuario que ingrese el valor a buscar
valor_a_buscar = int(input("Introduce el valor que deseas buscar en la matriz: "))

# Llamamos a la función para buscar el valor
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Mostramos un mensaje según si se encontró o no el valor
if resultado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_a_buscar} no se encontró en la matriz.")