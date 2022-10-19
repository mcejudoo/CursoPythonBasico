from random import randint
from functools import reduce

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def getTuple(self):   
        return (self.__hh, self.__mm, self.__ss)
   
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.__hh,self.__mm,self.__ss)


def laMenor(t1, t2):
    print(t1,"<==>",t2)
    tu1 = t1.getTuple()
    tu2 = t2.getTuple()
    return t1 if tu1 < tu2 else t2

if __name__ == '__main__':
    # Generar una lista de Time
    L = [Time(randint(0,23),randint(0,59),randint(0,59)) for _ in range(10)]

    # Con reduce seleccionar la pequeña
    menor = reduce(laMenor,L)
    print(menor)