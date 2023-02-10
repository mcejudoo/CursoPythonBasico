"""
Ejemplo de hilos: creación, puesta en marcha, espera ..
"""

from threading import Thread
from random import randint
from time import sleep

class HiloMensaje(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName()+' Mensaje: ', i)
            sleep(randint(0,2))
        print("Fin mensajes")

class HiloAleatorio(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('Aleatorio: ', randint(1,100))
            sleep(randint(1, 3))
        print('Fin aleatorio')

if __name__ == '__main__':
    mensajes = HiloMensaje(10)
    mensajes2 = HiloMensaje(6)
    aleatorio = HiloAleatorio(8)

    mensajes.start()    
    mensajes2.start()    
    aleatorio.start()

    mensajes.join()
    mensajes2.join()
    aleatorio.join()

    print('Fin main')
