"""
Generar datos aleatorios de una fecha del 2022 con su ingreso.
Calcular un histograma de ingresos mensuales y ordenar desc. por mes
"""
from datetime import date
from random import randint

def generarDatos(año=2022, n=100):
    """
    Genera una lista de tuplas indicando la fecha y el ingreso.
    """
    L = [(date(año, randint(1,12), randint(1,28)), randint(1000, 10000)) for _ in range(n)]
    return L

def histogramaMes(L):
    """
    Histograma mensual de ingresos
    """
    histo = dict()

    # imprimir el mes y el ingreso
    for t in L:
        fecha, ingreso = t
        mes = fecha.month
        if mes in histo:
            # Tenemos que acumular el ingreso:
            histo[mes] += ingreso

        else:
            # Es el primer ingreso del mes
            histo[mes] = ingreso

    return histo

def ordenarImprimir(histo):
    meses = {1:'Ene',2:'Feb',3:'Mar',4:'Abr',5:'May',6:'Jun', \
        7:'Jul',8:'Ago',9:'Sep',10:'Oct',11:'Nov',12:'Dic'}

    L = sorted(histo.items(), key=lambda t:t[1], reverse=True)
    ingresosTotales = sum([t[1] for t in L])
    
    for mes, ingreso in L:
        print(meses[mes],'\t',ingreso, '\t', round(ingreso/ingresosTotales*100,2),"%")

if __name__ == '__main__':
    L = generarDatos()   
    histo = histogramaMes(L)
    ordenarImprimir(histo)


