"""
Programación funcional en Python. map, filter, reduce, list comprehesion.
"""
import random
IVA = 0.21
ini = 20
fin = 40

def iva(precio):
    return round(precio * (1+IVA), 2)

def cumplenRango(valor):
    return True if ini <= valor <= fin else False

precios = [120.45, 330.6, 50, 100]    
preciosFinal = list(map(iva, precios))
print(precios)
print(preciosFinal)

preciosFinal2 = [iva(p) for p in precios]
print(preciosFinal2)
preciosFinal3 = [round(p * (1+IVA), 2) for p in precios]
print(preciosFinal3)

aleatorios = [random.randint(1,100) for _ in range(20)]
print(aleatorios)

# filter: filtrar números que están dentro de un rango
filtro1 = list(filter(cumplenRango, aleatorios))
print(filtro1)
print(sum(filtro1))
print(sum(filtro1)/len(filtro1))

filtro2 = [i for i in aleatorios if ini <= i <= fin]
print(filtro2)

prueba = [(i, 2**i) for i in range(10)]
print(prueba)

tablas = [(i,j,i*j) for i in range(1,11) for j in range(1,11)]
print(tablas[:10])




