"""
Ejemplo de hilos: creación, puesta en marcha, espera ..
"""

from threading import Thread
from random import randint

class HiloMensaje(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('Mensaje: ', i)
        print("Fin mensajes")

class HiloAleatorio(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('Aleatorio: ', randint(1,100))
        print('Fin aleatorio')

if __name__ == '__main__':
    mensajes = HiloMensaje(10)
    aleatorio = HiloAleatorio(8)

    mensajes.start()
    aleatorio.start()
    print('Fin main')
