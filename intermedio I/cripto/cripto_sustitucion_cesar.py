#-*- coding: utf-8 -*-

#funciones de codificación de letras en números;

alfabeto=' abcdefghijklmnopqrstuvwxyz'

def codificaLetra(letra):
    return alfabeto.index(letra)
    
def decodificaLetra(numero):
    return alfabeto[numero]

def codificaCadena2(cadena):
    L = []
    for letra in cadena:
        L.append(codificaLetra(letra))
    return L
    
def codificaCadena(cadena):
    return [codificaLetra(i) for i in cadena]
    
def decodificaCadena(numeros):
    return ''.join(decodificaLetra(i) for i in numeros)
    
def decodificaCadena2(numeros):
    s = ''
    for n in numeros:
        s+=decodificaLetra(n)
    return s

def cifradoCesar(texto,clave,alfabeto):
    #convertir el texto en una lista de numeros
    L = codificaCadena(texto)
    #print("texto:",texto)
    #print(L)
    
    #sumar a la lista la clave teniendo en cuenta la lon. del alf.
    lon = len(alfabeto)
    LL=[]
    for i in L:
        LL.append((i+clave)%lon)
        
    #print LL
    #convertir la lista de numeros en letras.
    return decodificaCadena(LL)
    
def descifrarCesar(texto,clave,alfabeto):
    clave = -clave
    return cifradoCesar(texto, clave, alfabeto)
    
    
textoCif = cifradoCesar('hola que tal', 7, alfabeto)
print (textoCif)
texto = descifrarCesar(textoCif, 7, alfabeto)
print (texto)
    
print (codificaCadena('hola'))
print (codificaCadena2('hola'))
print (decodificaCadena([8,15,12,1]))
print (decodificaCadena2([8,15,12,1]))
print (decodificaCadena(codificaCadena('hola')))

print (decodificaLetra(codificaLetra('f')))
