"""
Parámetros en las funciones de python
"""

def funcion2(*args):
    pass

def funcion3(*args, **kwargs):
    pass

def funcion(ob1, ob2, op1=10, op2=20, *args, **kwargs):
    print('Obligatorios: ', ob1, ob2)
    print('Opcionales: ', op1, op2)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()


if __name__ == '__main__':
    funcion(1,2)
    funcion(1,2,op2=200)
    funcion(1,2,3,4)
    funcion(1,2,3,4,5,6,7,8)
    funcion(1,2,3,4,5,6,7,8,x=10,y=20)
