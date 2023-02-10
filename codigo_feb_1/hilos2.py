"""
Ejemplo de condición de carrera con una variable compartida.
Utilización de mecanismos de sincronización (Locks)
"""

import threading
from threading import Thread, Lock

iteraciones = 1000000
contador = 0
contador2 = 0
mutex = Lock()

def sumar():
    global contador
    for i in range(iteraciones):
        contador += 1

def restar():
    global contador
    for i in range(iteraciones):
        contador -= 1

def sumar2():
    global contador2
    for i in range(iteraciones):
        mutex.acquire() # Comprobar si está el cerrojo
        contador2 += 1
        mutex.release() # Libera el cerrojo

def restar2():
    global contador2
    for i in range(iteraciones):
        with mutex: # Captura y libera el cerrojo automáticamente
            contador2 -= 1

if __name__ == '__main__':
    h1 = Thread(target=sumar)
    h2 = Thread(target=restar)
    h3 = Thread(target=sumar2)
    h4 = Thread(target=restar2)

    h1.start()
    h2.start()
    h3.start()
    h4.start()

    print(threading.enumerate())

    h1.join()
    h2.join()
    h3.join()
    h4.join()

    print('Contador: ', contador)
    print('Contador2: ', contador2)
