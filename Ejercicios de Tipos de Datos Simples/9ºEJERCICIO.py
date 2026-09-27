cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés anual (%): "))
anios = int(input("¿Número de años?: "))

# Convertimos el porcentaje de interés dividiendo por 100
capital_final = cantidad * (1 + interes / 100) ** anios
print("El capital obtenido en la inversión es:", round(capital_final, 2))