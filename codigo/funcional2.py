"""
Uso de funciones lambda en Python
"""

def ordenar(L, campo, sentido='asc'):
    campos = ['nombre','edad','altura']
    reverse = True if sentido == 'desc' else False
    pos = campos.index(campo)
    L.sort(key=lambda t:t[pos], reverse=reverse)

if __name__ == '__main__':
    L = [('Ana',34,1.77), ('Alberto',55,1.88), \
        ('Angelica',44,1.67),('Ramón',23,1.89), \
            ('Eva',45,1.87)]

    ordenar(L, 'altura', 'desc')
    print(L)
    ordenar(L, 'nombre', 'asc')
    print(L)
    exit()

    # Ordenar por distintos criterios: por nombre, por edad o por altura
    L.sort(reverse=True)
    print(L)  

    # Por edad DESC
    L.sort(key=lambda t:t[1], reverse=True)
    print(L)

    # Por Altura ASC:
    L.sort(key=lambda t:t[2])
    print(L)