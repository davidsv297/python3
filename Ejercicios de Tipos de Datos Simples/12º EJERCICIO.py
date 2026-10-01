precio_habitual = 3.49
descuento = 0.60  # 60% de descuento

barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

precio_con_descuento = precio_habitual * (1 - descuento)
coste_total = barras_no_frescas * precio_con_descuento

print("Precio habitual de una barra:", precio_habitual, "€")
print("Descuento por no ser fresca:", descuento * 100, "%")
print("Coste final total:", round(coste_total, 2), "€")