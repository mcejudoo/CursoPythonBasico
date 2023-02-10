"""
Implementación productor-consumidor en Python con semáforos y locks
"""

from threading import Thread, Semaphore, Lock
from time import sleep
from random import randint

num_muestras = 20
tam_buffer = 10

class Buffer:

    def __init__(self, size=10):
        self.mutex = Lock()
        self.items = Semaphore(0)
        self.huecos = Semaphore(size)
        self.iC = 0
        self.iP = 0
        self.buf = ['']*size

class Productor(Thread):

    def __init__(self, b):
        Thread.__init__(self)
        self.b = b        

    def run(self):
        for i in range(num_muestras):
            letra = chr(randint(65,65+25))
            print('P: ', letra)

            self.b.huecos.acquire() # Tengo hueco?
            with self.b.mutex:
                self.b.buf[self.b.iP] = letra
                self.b.iP = (self.b.iP + 1) % tam_buffer
                print('Buffer: ', self.b.buf)

            self.b.items.release() # Avisa al C. que ya tiene un item

            sleep(randint(0,1))

class Consumidor(Thread):

    def __init__(self, b):
        Thread.__init__(self)
        self.b = b        

    def run(self):
        for i in range(num_muestras):

            self.b.items.acquire() # Tengo un item?
            with self.b.mutex:
                letra = self.b.buf[self.b.iC]
                self.b.buf[self.b.iC] = ' '                
                self.b.iC = (self.b.iC + 1) % tam_buffer
                print('Buffer: ', self.b.buf)

            self.b.huecos.release()  # Avisar de que ya tiene un hueco

            print('C: ', letra)
            sleep(randint(1,3))

if __name__ == '__main__':
    b = Buffer(tam_buffer)
    p = Productor(b)
    c = Consumidor(b)

    p.start()
    c.start()

    p.join()
    c.join()