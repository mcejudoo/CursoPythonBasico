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

N = 30
n1 = 4
n2 = 100

#1) Generar una lista de N numeros aleatorios
aleatorios = []
for i in range(N):
    aleatorios+=[randint(0,n2-1)]
print(aleatorios[:5])

#2) Generar una estructura para almacenar los intervalos
intervalos = dict()
salto = n2 // n1
for i in range(0, n2, salto):
    t = (i,i+salto-1)
    intervalos[t] = list()
print(intervalos)    

#3) Repartir los números en los intervalos (almacenar)
for num in aleatorios:
    for a,b in intervalos.keys():
        if a <= num <= b:
            intervalos[(a,b)] += [num]
            break

#4) Imprimir resultados
print('Resultados:')
for t, L in intervalos.items():
    print(t,L)

print()    