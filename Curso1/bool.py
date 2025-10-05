numero = 42
cadena = "Hola"
vacio = ""

bool_numero = bool(numero)  # True, porque 42 es un valor no nulo
bool_cadena = bool(cadena)  # True, porque "Hola" es una cadena
bool_vacio = bool(vacio)    # False, porque es una cadena vacía

print("Booleano de numero:", bool_numero)
print("Booleano de cadena:", bool_cadena)
print("Booleano de vacio:", bool_vacio)