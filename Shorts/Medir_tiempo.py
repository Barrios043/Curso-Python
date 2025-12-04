import time

inicio = time.time()

#Aqui va el codigo que quieres medir
for i in range(100000000):
    pass

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"El tiempo de ejecución fue de {tiempo_ejecucion:.5f} segundos.")