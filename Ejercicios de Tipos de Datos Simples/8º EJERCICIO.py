n = int(input("Introduce el primer número entero (dividendo): "))
m = int(input("Introduce el segundo número entero (divisor): "))

c = n // m  # División entera (cociente)
r = n % m   # Módulo (resto)

print(n, "entre", m, "da un cociente", c, "y un resto", r)