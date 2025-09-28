# 8.Usando la condicional if imprimir por pantalla si una lista ([]) está vacía o no, comprobar con una lista vacía y otra con una lista con dato al menos ([dato_1, dato_2]).

lista_vacia = []
lista_con_datos = ["dato_1", "dato_2"]

def comprobar(lista):
    if not lista:
        print("La lista está VACÍA.")
    else:
        print("La lista NO está vacía. Contiene:", lista)

comprobar(lista_vacia)
comprobar(lista_con_datos)