"""
3. Crear una función funciona_indice(persona, indice) y dentro la respectiva
excepción para el siguiente bloque de código para que tu programa no se
bloquee y además imprime un mensaje al usuario: “El índice “nombre_indice”
ingresado no existe en el diccionario”, tipo de datos, etc que más pueden
incurrir para este caso (los datos se pedirán por consola):

persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion'] #El índice en este caso no existe

Usar la función al menos 2 veces incluyendo un caso de error
"""

def funciona_indice(persona, indice):
    try:
        valor = persona[indice]
        print(f"El valor para la clave '{indice}' es '{valor}'")
    except KeyError:
        print(f"Error: El índice '{indice}' ingresado no existe en el diccionario. Causa: La clave no está presente. Solución: Use una clave válida como {list(persona.keys())}.")
    except TypeError:
        print(f"Error: El índice '{indice}' no es válido. Causa: El índice debe ser una cadena (str). Solución: Ingrese una clave de tipo texto.")
    finally:
        print("Operación finalizada")

persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}

indice1 = input("Ingrese la primera clave a buscar (ej. nombre, apellido, dni): ")
funciona_indice(persona, indice1)

indice2 = input("Ingrese la segunda clave a buscar: ")
funciona_indice(persona, indice2)

print(f"Diccionario: {persona}")