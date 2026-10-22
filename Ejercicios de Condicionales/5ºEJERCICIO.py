edad = int(input("Ingrese su edad: "))
ingresosm = float(input("Ingrese sus ingresos mensuales: "))
if (edad >=18 and ingresosm >= 1000):
    print(f"Usted tiene {edad} años y sus ingresos son {ingresosm}€ por lo debe tributar")
else:
    print(f"Usted tiene {edad} años y sus ingresos son {ingresosm}€ por lo que no debe tributar")