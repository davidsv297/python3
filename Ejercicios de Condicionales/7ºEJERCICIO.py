renta = float(input("Ingrese su renta anual: "))

if renta < 10000:
    print ("El tipo de impositivo que te corresponde es 5%")
elif renta  > 10000 and renta <20000:
    print ("El tipo de impositivo que te corresponde es 15%")
elif renta  > 20000 and renta < 35000:
    print ("El tipo de impositivo que te corresponde es 20%")
elif renta  > 35000 and renta < 60000:
    print ("El tipo de impositivo que te corresponde es 30%")
else:
    print ("El tipo de impositivo que te corresponde es de 45%")