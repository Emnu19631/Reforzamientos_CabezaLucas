def saluda_fecha(nombre, dia, mes, año):
    try:
        if nombre.replace(" ", "").isdigit():
            print(f"Error: El nombre no debe ser numérico. Solución: Ingrese un nombre como texto.")
            print("Operación finalizada")
            return

        if mes.replace(" ", "").isdigit():
            print(f"Error: El mes no debe ser numérico. Solución: Ingrese un mes como texto.")
            print("Operación finalizada")
            return

        dia_num = int(dia)
        año_num = int(año)

        cadena = f"Hello {nombre}, hoy estamos {dia_num:02d} de {mes} del {año_num}"
        print(cadena)

    except ValueError:
        print(
            "Error: Día y año deben ser numéricos. Causa: Entrada no válida. Solución: Ingrese números enteros para día y año.")
    except TypeError:
        print(
            "Error: Entrada no válida. Causa: Los datos no son del tipo correcto. Solución: Ingrese texto para nombre y mes, y números para día y año.")
    finally:
        print("Operación finalizada")

nombre1 = input("Ingrese el nombre para caso 1: ")
dia1 = input("Ingrese el día para caso 1: ")
mes1 = input("Ingrese el mes para caso 1: ")
año1 = input("Ingrese el año para caso 1: ")
saluda_fecha(nombre1, dia1, mes1, año1)

nombre2 = input("Ingrese el nombre para caso 2: ")
dia2 = input("Ingrese el día para caso 2: ")
mes2 = input("Ingrese el mes para caso 2: ")
año2 = input("Ingrese el año para caso 2: ")
saluda_fecha(nombre2, dia2, mes2, año2)

nombre3 = input("Ingrese el nombre para caso 3: ")
dia3 = input("Ingrese el día para caso 3: ")
mes3 = input("Ingrese el mes para caso 3: ")
año3 = input("Ingrese el año para caso 3: ")
saluda_fecha(nombre3, dia3, mes3, año3)