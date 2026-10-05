# 1. Pedimos el número completo
telefono = input("Introduce un número de teléfono con el formato +34-número-extensión: ")

# 2. Dividimos el texto usando el guion '-' como separador
partes = telefono.split("-")

# 3. Mostramos solo la parte central (índice 1)
print(f"El número de teléfono sin prefijo ni extensión es: {partes[1]}")