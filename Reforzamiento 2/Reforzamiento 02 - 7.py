# 7.De 3 números asignados mayores a 30 (entre positivos y negativos tú los propones) a 3 variables, se pide hallar la suma de los valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma.

x = 35
y = -42
z = 31
suma = (abs(x) % 3) + (abs(y) % 5) + (abs(z) % 7)
print("Suma de módulos:", suma)
