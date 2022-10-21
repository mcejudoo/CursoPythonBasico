#!/usr/bin/env python
# -*- coding: utf-8 -*-

# serialización:
try:
        import cPickle as pickle
except:
        import pickle


def serializar(fich,obj):
        """ Serializa obj en fich"""
        try:
                fichero = open(fich, "wb")
                datos = [1,2,3,4,5,6,7,8,9]
                pickle.dump(datos, fichero, 2)
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

L = [1,2,3,7,45,5,6,7,8,89,9]

if serializar("datos.dat",L):
        
        obj = deserializar("datos.dat")
        if obj != None:
                print (obj)
        else:
                print ("Imposible recuperar")
else:
        print ("No ha sido posible serializar")
