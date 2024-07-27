import time

try:
    while True:
        print("Bucle infinito en ejecucion, precione Ctrl + C para salir")
        time.sleep(2)
except KeyboardInterrupt:
    print("Bucle infinito interrumpido")