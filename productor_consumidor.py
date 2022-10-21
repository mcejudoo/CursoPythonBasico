from threading import Thread, Lock, Semaphore
from time import sleep
from random import randint

BUFFER_SIZE = 15
NUM_ITEMS = 20

class Productor(Thread):
    
    def __init__(self, mutex, sem_huecos, sem_items, buffer,index_p, index_c):
        Thread.__init__(self)
        self.mutex = mutex
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.buffer = buffer
        self.index_c = index_c
        self.index_p = index_p

    def run(self):
        for i in range(NUM_ITEMS):
            item = randint(1,100)            
            sem_huecos.acquire()
            mutex.acquire()
            self.buffer[self.index_p] = item
            self.index_p = (self.index_p + 1) % BUFFER_SIZE
            print("PRODUCTOR:", item, self.buffer)
            mutex.release()
            sem_items.release()
            sleep(randint(0,1))

class Consumidor(Thread):
    
    def __init__(self, mutex, sem_huecos, sem_items, buffer,index_p, index_c):
        Thread.__init__(self)
        self.mutex = mutex
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.buffer = buffer
        self.index_c = index_c
        self.index_p = index_p

    def run(self):
        for i in range(NUM_ITEMS):
            sem_items.acquire()
            mutex.acquire()
            item = self.buffer[self.index_c]
            self.buffer[self.index_c] = 0
            self.index_c = (self.index_c + 1) % BUFFER_SIZE  
            print('CONSUMIDOR:', item, self.buffer)
            mutex.release()
            sem_huecos.release()           
            sleep(randint(1,3))


if __name__ == '__main__':
    index_p = index_c = 0
    mutex = Lock()
    sem_items = Semaphore(0)      
    sem_huecos = Semaphore(BUFFER_SIZE)
    buffer = [0] * BUFFER_SIZE

    p = Productor(mutex, sem_huecos, sem_items, buffer, index_p, index_c)
    p.start()

    c = Consumidor(mutex, sem_huecos, sem_items, buffer, index_p, index_c)
    c.start()

    p.join()
    c.join()