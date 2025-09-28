"""
4. Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)
"""
def contar_letras_nombre(nombre_completo):
    """Cuenta las letras del nombre (primera palabra) en el nombre completo."""
    nombre = nombre_completo.split()[0]  #
    cantidad_letras = len(nombre)
    print(f"El nombre '{nombre}' tiene {cantidad_letras} letras")
    return nombre, cantidad_letras

persona1 = input("Ingrese el nombre y apellidos de la primera persona: ")
persona2 = input("Ingrese el nombre y apellidos de la segunda persona: ")

nombre1, letras1 = contar_letras_nombre(persona1)
nombre2, letras2 = contar_letras_nombre(persona2)

if letras1 > letras2:
    print(f"El nombre con más letras es '{nombre1}' con {letras1} letras")
elif letras2 > letras1:
    print(f"El nombre con más letras es '{nombre2}' con {letras2} letras")
else:
    print(f"Los nombres '{nombre1}' y '{nombre2}' tienen el mismo número de letras: {letras1}")