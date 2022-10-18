"""
Control de flujo y colecciones: Se piden dos números, uno menor que 10 y otro 
mayor que 100. El primer número representa el número de intervalos 
y hay que calcular los rangos de los intervalos según el segundo número. 
Por ejemplo: n1 = 4, n2 = 100. Los rangos serían de 0..24, 25..49, 50..74, 75..99.
Después se generan número al azar que no sobrepasen el número n2 y 
se almacenan en cada intervalo. Luego listar los intervalos con los números 
que se han recogido
"""

# from modulo import funcion
from random import randint

# Definir una función para este script. 
# Con la opción de pasar o no los números a repartir
# Devuelve los intervalos rellenos
# Y recibir el número N, n1 y n2 (de forma opcional)

N = 30
n1 = 4
n2 = 100

def generarIntervalos(numeros=None,N=30, n1=4, n2=100):
    #1) Generar una lista de N numeros aleatorios
    if numeros:
        aleatorios = numeros
    else:
        aleatorios = []
        for i in range(N):
            aleatorios+=[randint(0,n2-1)]

    #2) Generar una estructura para almacenar los intervalos
    intervalos = dict()
    salto = n2 // n1
    for i in range(0, n2, salto):
        t = (i,i+salto-1)
        intervalos[t] = list()      

    #3) Repartir los números en los intervalos (almacenar)
    for num in aleatorios:
        for a,b in intervalos.keys():
            if a <= num <= b:
                intervalos[(a,b)] += [num]
                break

    return intervalos

if __name__ == "__main__":
    #4) Imprimir resultados
    intervalos = generarIntervalos(N=20, n1=2)
    print('Resultados:')
    for t, L in intervalos.items():
        print(t,L)

    print()   