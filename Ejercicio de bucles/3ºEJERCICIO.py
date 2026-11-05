numero = int(input("Introduce un número: "))

for i in (1, numero +1, 2):
    if i + 2 <= numero:
        print(i, end=", ")
    else :
        print(i)