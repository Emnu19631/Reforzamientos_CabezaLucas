# 12. Escribe un programa que almacene información de un producto: Tu
# nombre, nombre del producto, precio unitario (float), cantidad (int) e
# imprimirá finalmente algo como lo siguiente:
# Buen día Nombre, el detalle de su compra es el siguiente:
# - Producto: Pollo a la brasa
# - Precio unitario: 50.50
# - Cantidad: 2
# - Total a pagar: 101

nombre = "Buen día Juan"
producto = "Pollo a la brasa"
precio_unitario = 50.50
cantidad = 2
total = precio_unitario * cantidad
print(f"{nombre}, el detalle de su compra es el siguiente:")
print(f"- Producto: {producto}")
print(f"- Precio unitario: {precio_unitario}")
print(f"- Cantidad: {cantidad}")
print()
print(f"- Total a pagar: {total:.0f}")
