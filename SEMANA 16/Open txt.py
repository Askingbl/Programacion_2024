# Ejemplo de Apertura de Archivos en Python

# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Modo de apertura: "r" para lectura (read)
# Abrimos el archivo que acabamos de crear
archivo = open(file_name, "w")

archivo.write('1. Mi nombres Carlos Pazmiño\n')
archivo.write('2. Tengo 30 años\n')
archivo.write('3. soy de Lago Agrio\n')

# Cerramos el archivo después de leer
archivo.close()

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Metodo read(): lee todo el archivo
contenido_completo = archivo_lectura.read()
print("Contenido completo usando read():")
print(contenido_completo)

# Metodo readline(): lee una línea a la vez
archivo_lectura.seek(0)  # Reiniciamos el cursor al principio del archivo
linea_1 = archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()

print("\nContenido línea por línea usando readline():")
print(linea_1.strip())  # strip() elimina el salto de línea al final
print(linea_2.strip())
print(linea_3.strip())

# Cerramos el archivo de lectura
archivo_lectura.close()