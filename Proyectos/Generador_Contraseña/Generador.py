import string
import random

def generar_contrasena(longitud):
    caracteres = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*+-")
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

longitud = int(input("Cual es la longitud de la contraseña que deseas generar?: "))

nueva_contrasena = generar_contrasena(longitud)
print("Tu nueva contraseña es: ", nueva_contrasena)