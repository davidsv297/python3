# Pedimos la fecha al usuario
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Separamos el texto usando la barra '/' como separador
partes = fecha.split('/')

# Guardamos cada parte en una variable (recordemos que en programación empezamos a contar desde el 0)
dia = partes[0]
mes = partes[1]
anyo = partes[2]

# Mostramos el resultado por pantalla
print("Día:", dia)
print("Mes:", mes)
print("Año:", anyo)