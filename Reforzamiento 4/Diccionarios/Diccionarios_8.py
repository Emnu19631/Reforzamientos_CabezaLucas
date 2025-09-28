"""
8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""

agenda = {}

while True:
    print("\n1. Agregar persona a la agenda")
    print("2. Buscar persona en la agenda")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el número de teléfono de {}: ".format(nombre))
        agenda[nombre] = telefono
        print("¡{} ha sido registrado en la agenda!".format(nombre))

    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        if nombre_buscar in agenda:
            print("{} tiene el número de teléfono: {}".format(nombre_buscar, agenda[nombre_buscar]))
        else:
            print("No se encuentra registrado en la agenda")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor seleccione 1, 2 o 3.")

print("Agenda final: {}".format(agenda))