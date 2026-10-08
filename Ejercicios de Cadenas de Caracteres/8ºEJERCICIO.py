precio_de_producto = input("Introduce el precio del producto: ")
partes_precio = precio_de_producto.split(".")

print (f"El precio del producto es: {partes_precio[0]} euros y {partes_precio[1]} céntimos" )