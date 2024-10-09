import time
def temporazidor(func):
    def envoltura():
        inicio = time.time()
        func()
        fin = time.time()
        print (f"Tiempo de ejecucion {fin - inicio} segundos")
    return envoltura
@temporazidor
def funcion_demorada():
    time.sleep(2)

funcion_demorada()