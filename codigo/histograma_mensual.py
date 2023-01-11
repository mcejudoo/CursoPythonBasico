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
        print(fecha.month, ingreso)

if __name__ == '__main__':
    L = generarDatos(n=5)
    #print(L[:5])
    histogramaMes(L)



