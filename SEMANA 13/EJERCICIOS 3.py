# Lista de ciudades para el menú
ciudades_nombres = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Matriz 3D de temperaturas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Crear un menú para seleccionar una ciudad y una semana
def mostrar_menu_ciudades():
    print("Seleccione una ciudad para ver los promedios de temperatura:")
    for i, ciudad in enumerate(ciudades_nombres, start=1):
        print(f"{i}. {ciudad}")
    while True:
        try:
            eleccion = int(input("Ingrese el número de la ciudad: ")) - 1
            if 0 <= eleccion < len(temperaturas):
                return eleccion
            else:
                print("Selección no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def mostrar_menu_semanas():
    print("\nSeleccione una opción para ver el promedio:")
    print("1. Promedio de todas las semanas")
    print("2. Promedio de una semana específica")
    print("3. Promedio general de la ciudad")
    while True:
        try:
            eleccion = int(input("Ingrese su elección: "))
            if eleccion in [1, 2, 3]:
                return eleccion
            else:
                print("Selección no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def mostrar_menu_semana_especifica():
    while True:
        try:
            semana = int(input("Ingrese el número de la semana (1 a 4): ")) - 1
            if 0 <= semana < 4:
                return semana
            else:
                print("Selección no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número válido.")

# Calcular y mostrar el promedio de temperaturas para la ciudad seleccionada
def mostrar_promedios_ciudad(ciudad_index):
    ciudad = temperaturas[ciudad_index]
    eleccion_semanas = mostrar_menu_semanas()

    if eleccion_semanas == 1:  # Promedio de todas las semanas
        print(f"\nPromedios de temperatura para {ciudades_nombres[ciudad_index]} en todas las semanas:")
        for j, semana in enumerate(ciudad):
            suma = sum(dia['temp'] for dia in semana)
            promedio = suma / len(semana)
            print(f"  Semana {j + 1}: Promedio de temperatura: {promedio:.2f}°F")
    elif eleccion_semanas == 2:  # Promedio de una semana específica
        semana_index = mostrar_menu_semana_especifica()
        semana = ciudad[semana_index]
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"\nSemana {semana_index + 1}: Promedio de temperatura: {promedio:.2f}°F")
    elif eleccion_semanas == 3:  # Promedio general de la ciudad
        total_dias = 0
        suma_total = 0
        for semana in ciudad:
            suma_total += sum(dia['temp'] for dia in semana)
            total_dias += len(semana)
        promedio_general = suma_total / total_dias
        print(f"\nPromedio general de temperatura para {ciudades_nombres[ciudad_index]}: {promedio_general:.2f}°F")

    print()

# Programa principal
while True:
    eleccion_ciudad = mostrar_menu_ciudades()  # Mostrar menú y obtener selección de ciudad
    mostrar_promedios_ciudad(eleccion_ciudad)  # Mostrar promedios de la ciudad seleccionada
    continuar = input("¿Desea consultar otra ciudad? (s/n): ").lower()
    if continuar != 's':
        print("Saliendo del programa...")
        break
