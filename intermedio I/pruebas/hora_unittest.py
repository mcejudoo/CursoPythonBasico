#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class Time(object):

    def __init__(self,hh=0,mm=0,ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    # Getters, Setters.
    def getHH(self):
        return self.__hh

    def setHH(self,hh):
        self.__hh = hh

    def getMM(self):
        return self.__mm

    def setMM(self,mm):
        self.__mm = mm

    def getSS(self):
        return self.__ss

    def setSS(self,ss):
        self.__ss = ss


    # definición de propiedades:
    hh = property(getHH, setHH)
    mm = property(getMM, setMM)
    ss = property(getSS, setSS)
    
    def __str__(self):
        #return str(self.__hh) + ":" + str(self.__mm) + ":" + str(self.__ss)
        return '%02d:%02d:%02d' % (self.__hh,self.__mm,self.__ss)


    def __add__(self,hora2):      
        segundos = self.__ss + hora2.__ss
        minutos = self.__mm + hora2.__mm
        horas = self.__hh + hora2.__hh

        if segundos > 59:
            segundos -= 60
            minutos += 1

        if minutos > 59:
            minutos -= 60
            horas += 1

        horas %= 24
        return Time(horas,minutos,segundos)

    def toSegundos(self):
        return self.__hh * 3600 + self.__mm * 60 + self.__ss


class testTime(unittest.TestCase):

    def setUp(self):
        print ("inicializar contexto")
        

    def testSuma(self):
        print ("test suma")
        t1 = Time(2,34,56)
        t2 = Time(3,56,5)
        t3 = t1 + t2
        self.assertEqual(str(t3),'06:31:1')
        

    def tearDown(self):
        print ("cerrar contexto")


if __name__ == "__main__":
        unittest.main()
