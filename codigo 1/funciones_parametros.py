"""
Tipos de parámetros en una función
"""

def funcion(ob1,ob2,op1=1,op2=2,*args,**kwargs):
    print('Obligatorios: ',ob1,ob2)
    print('Opcionales:', op1,op2)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()


funcion(10,20)
funcion(10,20,op2=200)
funcion(1,2,3,4)
funcion(1,2,3,4,5,6,7,8)
funcion(1,2,3,4,5,6,7,8,x=10,y=12)

