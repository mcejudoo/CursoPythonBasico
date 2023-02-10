"""
Ejemplo de condición de carrera con una variable compartida.
Utilización de mecanismos de sincronización (Locks)
"""

from threading import Thread

iteraciones = 1000000
contador = 0

def sumar():
    global contador
    for i in range(iteraciones):
        contador += 1

def restar():
    global contador
    for i in range(iteraciones):
        contador -= 1

if __name__ == '__main__':
    h1 = Thread(target=sumar)
    h2 = Thread(target=restar)

    h1.start()
    h2.start()

    h1.join()
    h2.join()

    print('Contador: ', contador)
