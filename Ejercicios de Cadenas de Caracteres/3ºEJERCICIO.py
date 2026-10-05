# 1. Pedimos el nombre al usuario
nombre = input("Introduce tu nombre: ")

# 2. Convertimos el nombre a mayúsculas y contamos sus letras
nombre_mayus = nombre.upper()
numero_letras = len(nombre)

# 3. Mostramos el resultado por pantalla
print(f"{nombre_mayus} tiene {numero_letras} letras")