"""3. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes."""


persona = {'nombre': "Ayrton Gonzales",'edad': 22,'salario': 1800}

lista_persona = list(persona.items())

print("Tipo de datos final: {}".format(type(lista_persona)))