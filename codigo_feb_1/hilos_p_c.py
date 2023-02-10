"""
Implementación productor-consumidor en Python con semáforos y locks
"""

from threading import Thread, Semaphore, Lock
from time import sleep
from random import randint

num_muestras = 20

class Buffer:

    def __init__(self, size=10):
        self.mutex = Lock()
        self.items = Semaphore(0)
        self.huecos = Semaphore(size)
        self.iC = 0
        self.iP = 0
        self.buf = list()

class Productor(Thread):

    def __init__(self, b):
        Thread.__init__(self)
        self.b = b        

    def run(self):
        for i in range(num_muestras):
            sleep(randint(0,2))

class Consumidor(Thread):

    def __init__(self, b):
        Thread.__init__(self)
        self.b = b        

    def run(self):
        for i in range(num_muestras):
            sleep(randint(0,1))

if __name__ == '__main__':
    b = Buffer()
    p = Productor(b)
    c = Consumidor(b)

    p.start()
    c.start()

    p.join()
    c.join()