"""3. Crear una función que sume los dígitos del número ingresado y muestre
por consola la suma de todos estos dígitos."""

def suma_digitos(numero):
    """Calcula y muestra la suma de los dígitos de un número."""
    suma = sum(int(digito) for digito in str(numero))
    print(f"La suma de los dígitos de {numero} es {suma}")

try:
    numero = int(input("Ingrese un número: "))
    suma_digitos(numero)
except ValueError:
    print("Error: Ingrese un número entero válido.")