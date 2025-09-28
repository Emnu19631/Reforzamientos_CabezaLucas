
"""1. Dada una frase u oración encontrar que palabra es la que tiene más
caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres"""

frase = input("Ingrese una frase u oración: ")

palabras = frase.split()

palabra_mas_larga = max(palabras, key=len)

caracteres = len(palabra_mas_larga)

print("“{}” – {} caracteres".format(palabra_mas_larga, caracteres))