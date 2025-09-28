"""Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal."""

persona = {'nombre': "Emanuel Cabeza", 'edad': 23,'salario': 2500}

lista_persona = list(persona.items())

print("Diccionario original: {}".format(persona))
print("Diccionario convertido a lista: {}".format(lista_persona))