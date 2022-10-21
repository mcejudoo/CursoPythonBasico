"""
Implementación de dos hilos
"""

from threading import Thread
from random import randint
from time import sleep

class Aleatorios(Thread):

    def __init__(self, n):
        Thread.__init__(self, name="Aleatorios")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name,randint(1,20))
            sleep(randint(1,2))
        print(self.name,"FIN")

class Mensaje(Thread):

    def __init__(self, n):
        Thread.__init__(self, name="Mensajes")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name,"mensaje",i)    
            sleep(randint(1,3)) 
        print(self.name,"FIN")

if __name__ == '__main__':
    ale = Aleatorios(10)
    men = Mensaje(15)
    ale.start()
    men.start()
    ale.join()
    men.join()

    print('Hilo principal termina')




