
"""
2. Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""


frase = input("Coloque unas frase:")

frase = frase.lower()

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

print(f"a: {a}")
print(f"e: {e}")
print(f"i: {i}")
print(f"o: {o}")
print(f"u: {u}")