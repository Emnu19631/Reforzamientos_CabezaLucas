"""5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u"""

departamentos = {'Lima': "Capital", 'Arequipa': "Ciudad Blanca", 'Cusco': "Ciudad Imperial",'Piura': "Ciudad del Sol", 'Loreto': "Selva",'Puno': "Altiplano"}

departamentos["Carrera"] = "Ingeniería de Sistemas"

carrera = departamentos["Carrera"]

persona = {'nombre': "Emanuel Cabeza", 'edad': 23,'salario': 2500}
nombre = persona["nombre"]

print("Carrera: {}".format(carrera))
print("Nombre: {}".format(nombre))