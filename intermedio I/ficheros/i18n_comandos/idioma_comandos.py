#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class IdiomaException(Exception):

        def __init__(self,msg):
                self.__msg = msg

        def __str__(self):
                return self.__msg
        

class Idioma(object):

        def __init__(self,codigo):
                self.__diccionario = {}
                self.__codigo = codigo
                self.__load()
           

        def __load(self):
                path = "lang\\" + self.__codigo + ".txt"
                try:
                        f = open(path)
                        while True: 
                                linea = f.readline() 
                                if not linea:
                                        break
                                pos = linea.find('=')
                                if pos >= 0:
                                        # cargar el dic.
                                        clave = linea[:pos]

                                        if "\n" in linea[pos+1:]:
                                                valor = linea[pos+1:-1]
                                        else:
                                                valor = linea[pos+1:]
                                                
                                        self.__diccionario[clave]=valor                                                                
                                         
                except IOError:
                        raise IdiomaException("Código de País " + self.__codigo + " no soportado")
                finally:
                        f.close()
                
        def test(self):
                for k in self.__diccionario.keys():
                        print (k, "->", self.__diccionario[k])
       
        def getString(self,clave):
                if clave not in self.__diccionario:
                        raise IdiomaException("La clave " + clave + " no existe")
                else:
                        return self.__diccionario[clave]


# codigo de prueba:
if len(sys.argv) <= 1:
        print ("Se requieren parametros: python idioma_comandos -es | -en | -h")
        exit()

opcion = sys.argv[1][1:]
print ("opcion: ", opcion)

if opcion == "h":
        print ("uso del comando: python idioma_comandos.py -es | -en")
else:               
        try:         
                idioma = Idioma(opcion)
                print (idioma.getString("cv"))
                print ()
                #idioma.test()
        
        except IdiomaException as e:
                print (e)
                
        except Exception as e2:
                print (str(e2))
