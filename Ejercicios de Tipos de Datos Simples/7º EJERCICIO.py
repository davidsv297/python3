peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = peso / (estatura ** 2)
# round(imc, 2) redondea a 2 decimales
print("Tu índice de masa corporal es", round(imc, 2))