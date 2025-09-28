
"""
Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""

alumnos_notas = {}
cantidad = int(input("Ingrese la cantidad de alumnos: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del alumno {}: ".format(i+1))
    nota = float(input("Ingrese la nota de {}: ".format(nombre)))
    alumnos_notas[nombre] = nota

for nombre, nota in alumnos_notas.items():
    print("{} tiene la nota de {}".format(nombre, nota))

media = sum(alumnos_notas.values()) / len(alumnos_notas)
print("La media de las notas es: {}".format(media))