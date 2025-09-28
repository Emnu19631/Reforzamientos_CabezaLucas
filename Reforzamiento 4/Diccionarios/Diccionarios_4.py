"""4. Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario."""

departamentos = {'Lima': "Capital", 'Arequipa': "Ciudad Blanca", 'Cusco': "Ciudad Imperial",'Piura': "Ciudad del Sol", 'Loreto': "Selva",'Puno': "Altiplano"}

del departamentos["Piura"]

departamentos['Loreto'] = "Amazonas"

print("¿Piura está en el diccionario?: {}".format("Piura" in departamentos))

print("Diccionario actualizado: {}".format(departamentos))