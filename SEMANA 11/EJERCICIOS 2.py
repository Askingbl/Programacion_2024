def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriz 3x3 con valores numéricos
matrix = [
    [9, 3, 5],
    [7, 1, 6],
    [2, 8, 4]
]

print("Matriz original:")
print_matrix(matrix)

# Solicitar al usuario que ingrese el número de la fila que desea ordenar
try:
    row_to_sort = int(input("\nIngresa el número de la fila que deseas ordenar (0, 1, 2): "))
    if 0 <= row_to_sort < len(matrix):
        # Ordenar la fila seleccionada por el usuario
        bubble_sort(matrix[row_to_sort])

        print(f"\nMatriz después de ordenar la fila {row_to_sort}:")
        print_matrix(matrix)
    else:
        print("Número de fila inválido. Por favor, ingresa un número entre 0 y 2.")
except ValueError:
    print("Por favor, ingresa un número válido.")