"""9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”

Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado."""

facturas = {}

while True:
    print("\n1. Agregar nueva factura")
    print("2. Pagar factura")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        numero_factura = input("Ingrese el número de factura (ej. 00054): ")
        try:
            coste = float(input("Ingrese el coste de la factura: "))
            facturas[numero_factura] = coste
            print("Factura {} agregada.".format(numero_factura))
        except ValueError:
            print("Error: El coste debe ser un valor numérico.")
        print("Facturas pendientes: {}".format(facturas))

    elif opcion == "2":
        numero_factura = input("Ingrese el número de factura a pagar: ")
        if numero_factura in facturas:
            del facturas[numero_factura]
            print("La factura {} ya está cancelada.".format(numero_factura))
        else:
            print("El número de factura {} no existe.".format(numero_factura))
        print("Facturas pendientes: {}".format(facturas))

    elif opcion == "3":
        print("Saliendo del programa...")
        print("Facturas pendientes finales: {}".format(facturas))
        break

    else:
        print("Opción no válida, por favor seleccione 1, 2 o 3.")