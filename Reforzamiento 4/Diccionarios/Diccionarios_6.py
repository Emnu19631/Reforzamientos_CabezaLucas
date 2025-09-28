"""6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""


numeros_cubos = {}

for i in range(4):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros_cubos[numero] = numero ** 3

print("Diccionario con números y sus cubos: {}".format(numeros_cubos))