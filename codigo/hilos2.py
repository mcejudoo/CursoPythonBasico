"""
Implementación de dos hilos sumador / restador
"""

from threading import Thread, Lock
from random import randint
from time import sleep

contador = 0
iteraciones = 1000000

class Sumador(Thread):

    def __init__(self, mutex):
        Thread.__init__(self, name="Sumador")
        self.mutex = mutex
        
    def run(self):
        global contador
        for i in range(iteraciones):
            self.mutex.acquire()
            contador += 1   # Nos aseguramos que se ejecuta en exclusión mutua
            self.mutex.release()
        

class Restador(Thread):

    def __init__(self, mutex):
        Thread.__init__(self, name="Restador")
        self.mutex = mutex
        
    def run(self):
        global contador
        for i in range(iteraciones):
            with self.mutex:
                contador -= 1            

if __name__ == '__main__':
    mutex = Lock()

    s = Sumador(mutex)
    r = Restador(mutex)
    s.start()
    r.start()
        
    r.join()
    s.join()

    print('Contador: ', contador)



