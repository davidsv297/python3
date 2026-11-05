pizza = input("Dime que tipo de pizza deseas (Vegetariana/No Vegetariana)")
ingre = ""
if pizza.lower() == "vegetariana" :
    print ("Ingredientes vegetarianos: Pimiento y Tofu.")
    ingre = input("Que ingrediente desea escoge 1: ")
elif pizza.lower() == "no vegetariana" :
    print ("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
    ingre = input("Que ingrediente desea escoge 1: ")

print (f"Has escogido la pizza {pizza} sus ingredientes son Mozzarella, Tomate y {ingre}")