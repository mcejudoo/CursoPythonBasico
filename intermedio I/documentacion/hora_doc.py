#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Time(object):
    """La clase Time permite la gestión y operaciones con horas"""

    def __init__(self,hh=0,mm=0,ss=0):
        """ Constructor inicializa horas con h,m,s"""
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
        """ Convertir un Time a texto """
        #return str(self.__hh) + ":" + str(self.__mm) + ":" + str(self.__ss)
        return '%02d:%02d:%02d' % (self.__hh,self.__mm,self.__ss)


    def __add__(self,hora2):
        """ Sumar dos Time """
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
        """ Convertir a segundos un Time """
        return self.__hh * 3600 + self.__mm * 60 + self.__ss
