#!/usr/bin/env python
# -*- coding: utf-8 -*-

# serialización:
try:
        import cPickle as pickle
except:
        import pickle

class Punto:

        def __init__(self,x,y):
                self.x = x
                self.y = y

        def __str__(self):
                return "(" + str(self.x) + ", " + str(self.y) + ")"


def serializar(fich,obj):
        """ Serializa obj en fich"""
        try:
                fichero = open(fich, "wb")                
                pickle.dump(obj, fichero, 2)
                return True
        
        except Exception as e:
                print (e)
                return False

        finally:        
                fichero.close()


def deserializar(fich):
        """ Devuelve el obj."""
        try:
                fichero = open(fich,"rb")
                obj = pickle.load(fichero)
                return obj
        
        except Exception as e:
                print (e)
                return None
        
        finally:
                fichero.close()
                
        
# codigo principal:
print (pickle.__name__)

obj = Punto(1,3)

if serializar("datos.dat",obj):
        
        obj = deserializar("datos.dat")
        if obj != None:
                print(obj)
        else:
                print("Imposible recuperar")
else:
        print("No ha sido posible serializar")
