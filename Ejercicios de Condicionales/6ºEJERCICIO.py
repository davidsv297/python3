nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

uncarcnombre = nombre[0].upper()
sexo = sexo.upper()

if (sexo == "F" and uncarcnombre < "M") or (sexo == "M" and uncarcnombre > "N"):
    print("Te corresponde el Grupo A")
else:
    print("Te corresponde el Grupo B")