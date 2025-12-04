import random
def generar_contrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
nueva_contrasena = generar_contrasena(longitud)
print("Tu nueva contraseña es:", nueva_contrasena)