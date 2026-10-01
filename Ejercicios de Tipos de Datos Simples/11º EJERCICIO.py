deposito = float(input("Introduce la cantidad de dinero depositada: "))
interes = 0.04

anio_1 = deposito * (1 + interes)
anio_2 = anio_1 * (1 + interes)
anio_3 = anio_2 * (1 + interes)

print("Ahorros tras el primer año:", round(anio_1, 2))
print("Ahorros tras el segundo año:", round(anio_2, 2))
print("Ahorros tras el tercer año:", round(anio_3, 2))