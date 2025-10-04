#@title
#Utiliza la funcion "enumerate" al iterar sobre listas
nombres = ['Ana', 'Carlos', 'Sofía']
for indice, nombre in enumerate(nombres):
    print(indice, nombre)

#@title
"""Usa "list comprehensions" para crear listas de forma
consisa y leible"""
numeros = [1, 2, 3, 4, 5]
cuadrados = [numeros ** 2 for numeros in numeros]
print(cuadrados)

#@title
"""Aprovecha las funciones "lambda" para crear funciones
pequeñas y anonimas de manera rapida y sencilla"""
suma = lambda a, b: a + b
resultado = suma(3, 4)
print(resultado)