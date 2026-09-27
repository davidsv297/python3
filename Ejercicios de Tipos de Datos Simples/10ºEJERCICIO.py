peso_payaso = 112
peso_muneca = 75

payasos = int(input("Introduce el número de payasos vendidos: "))
munecas = int(input("Introduce el número de muñecas vendidas: "))

peso_total = (payasos * peso_payaso) + (munecas * peso_muneca)
print("El peso total del paquete es:", peso_total, "g")