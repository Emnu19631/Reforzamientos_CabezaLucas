"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""

persona = {'nombre': "Emanuel Cabeza",'edad': 23,'salario': 2500}

persona["dni"] = "121122001"

print("Salario: {}".format(persona["salario"]))
print("DNI: {}".format(persona["dni"]))

del persona["edad"]

print("Diccionario actualizado: {}".format(persona))