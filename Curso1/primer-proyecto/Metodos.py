nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + " " + apellido # Concatenacion de cadenas
longitud = len(nombre_completo) # Longitud de la cadena
nombre_mayusculas = nombre_completo.upper() # Convertir a mayusculas
nombre_minusculas = nombre_completo.lower() # Convertir a minusculas
posicion = nombre_completo.find("Perez") # Buscar posicion de un caracter o subcadena
nombre_reemplazado = nombre_completo.replace("Juan", "Carlos") # Reemplazar subcadena

print("Nombre Completo:", nombre_completo)
print("Longitud:", longitud)
print("Mayusculas:", nombre_mayusculas)
print("Minusculas:", nombre_minusculas)
print("Posicion de 'Perez':", posicion)
print("Reemplazado:", nombre_reemplazado)