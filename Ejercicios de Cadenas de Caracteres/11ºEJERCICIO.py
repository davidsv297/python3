producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
numero = int(input ("Ingrese la cantidad de productos: "))

coste_total = precio * numero

print(f"El producto es {producto} su precio unitario es {precio:09.2f} el numero de unidades es {numero:03d} y el coste total es {coste_total:011.2f}")