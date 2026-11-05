edad = float(input("Dime que edad tienes: "))

if edad <= 4 :
    print ('Puedes entrar gratis')
elif edad > 4 and edad < 18 :
    print ("Debe pagar 5€")
else :
    print ("Debe pagar 10€")
