"""
Prueba de hilos con Python
"""
from threading import Thread
from random import randint
from time import sleep

class HiloAleatorio(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('Aleatorio:', randint(0, 10))
            sleep(randint(0,2))

        print('Fin hilo Aleatorio')


class HiloMensaje(Thread):  

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n

    def run(self):
        for i in range(self.n):
            print('Mensaje:', i)
            sleep(randint(0,2))

        print('Fin hilo Mensaje')

if __name__ == '__main__':
    hilo1 = HiloAleatorio(8)        
    hilo2 = HiloMensaje(12)

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()
    print('Termina main ...')



