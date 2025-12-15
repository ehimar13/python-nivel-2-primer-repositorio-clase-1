###
import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

# Crea una variable y pide al usuario que introduzca la longitud de la contraseña
length = int(input("que longitud quieres que tenga la contranseña? "))

# Crea una variable en la que el programa almacenará la contraseña generada
clave = ""

# Utiliza un bucle y la librería random para seleccionar un carácter 
# aleatorio de la variable character y añadirlo a la variable con 
# la contraseña generada


for i in range(length):
    simbolo = random.choice(caracteres)
    clave += simbolo

print("la contrasena generada es", clave)
