def externa():
    x = 10

    def interna():
        print(x)

    interna()

externa() #Salida : 10