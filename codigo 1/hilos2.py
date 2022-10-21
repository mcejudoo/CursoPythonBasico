"""
Implementación de dos hilos sumador / restador
"""

from threading import Thread
from random import randint
from time import sleep

contador = 0
iteraciones = 1000000

class Sumador(Thread):

    def __init__(self):
        Thread.__init__(self, name="Sumador")
        
    def run(self):
        global contador
        for i in range(iteraciones):
            contador += 1   
        

class Restador(Thread):

    def __init__(self):
        Thread.__init__(self, name="Restador")
        
    def run(self):
        global contador
        for i in range(iteraciones):
            contador -= 1

if __name__ == '__main__':
    s = Sumador()
    r = Restador()
    s.start()
    r.start()
        
    r.join()
    s.join()

    print('Contador: ', contador)




