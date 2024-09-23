# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Catálogo de productos con opciones de descuentos
def mostrar_catalogo():
    catalogo = [
        {"producto": "Camiseta", "precio": 25.0, "descuento": 10},  # 10% de descuento
        {"producto": "Zapatos", "precio": 50.0, "descuento": 15},  # 15% de descuento
        {"producto": "Gorra", "precio": 15.0, "descuento": 0}  # Sin descuento
    ]

    while True:
        # Mostrar las opciones disponibles en el catálogo
        print("\nCatálogo de productos:")
        for idx, item in enumerate(catalogo, 1):
            nombre = item["producto"]
            print(f"{idx}. {nombre}")

        # Solicitar al usuario que elija los productos
        seleccionados = input(
            "\nSeleccione el producto que desea ver (ingrese el número, ej. 1,2): ")
        seleccionados = [int(num) - 1 for num in seleccionados.split(",") if
                         num.isdigit() and 0 < int(num) <= len(catalogo)]

        print("\nProductos seleccionados:")
        for idx in seleccionados:
            item = catalogo[idx]
            nombre = item["producto"]
            precio = item["precio"]
            descuento = item["descuento"]

            # Solicitar la cantidad de unidades para el producto seleccionado
            cantidad = int(input(f"Ingrese la cantidad de {nombre} que desea comprar: "))

            # Calcular el total sin descuento
            total_sin_descuento = precio * cantidad
            monto_descuento = calcular_descuento(precio, descuento)
            precio_final_unidad = precio - monto_descuento
            total_con_descuento = precio_final_unidad * cantidad

            # Mostrar la información organizada
            print(f"\nProducto: {nombre}")
            print(f"Precio por unidad: ${precio:.2f}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio total sin descuento: ${total_sin_descuento:.2f}")
            print(f"Descuento: {descuento}% - ${monto_descuento * cantidad:.2f} total")
            print(f"Precio final con descuento: ${total_con_descuento:.2f}")

        # Preguntar si desea volver al catálogo
        continuar = input("\n¿Desea volver al catálogo? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por su compra. ¡Hasta luego!")
            break


# Ejecutar la función para mostrar el catálogo y permitir la selección
mostrar_catalogo()

