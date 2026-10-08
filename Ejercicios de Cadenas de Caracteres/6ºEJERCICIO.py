frase = input("Introduce una frase:")
vocal = input("Introduce una vocal: ")

frase_vocal_mayus = frase.replace(vocal.lower(), vocal.upper())

print (f"La frase con la vocal en mayúscula es: {frase_vocal_mayus}")