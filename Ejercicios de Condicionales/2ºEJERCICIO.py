contraseña = "contraseña123".lower()

pedir_contra = input("Introduce la contraseña: ").lower()

if pedir_contra == contraseña :
    print("¡Contraseña correcta!")
else :
    print("Contraseña incorrecta.")