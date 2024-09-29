# Crear un Diccionario llamado 'informacion_personal'
# Los diccionarios en Python nos permiten almacenar datos en pares clave-valor
informacion_personal = {
    "nombre": "Carlos López",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceder y Modificar Valores
# Cambiamos el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"  # Modificamos la ciudad a Guayaquil

# Agregar una nueva clave-valor
# Ya existe la clave "profesion", pero podemos actualizar el valor
informacion_personal["profesion"] = "Ingeniero de Sistemas"  # Actualizamos la profesión

# Verificar Existencia de Claves
# Comprobamos si existe la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Agregamos un número de teléfono si no existe

# Eliminar una Clave
# Eliminamos la clave "edad" porque no es necesaria
informacion_personal.pop("edad", None)  # Usamos pop() para eliminar la clave de manera segura

# Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)
