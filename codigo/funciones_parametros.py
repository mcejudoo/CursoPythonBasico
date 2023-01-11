"""
Tipos de parámetros en una función de Python
"""

def params(ob1,ob2,op1=10,op2=20, *args, **kwargs):
    print("obligatorios: ", ob1, ob2)
    print("opcionales: ", op1, op2)
    print('args: ', args)
    print('kwargs: ', kwargs)
    print()


if __name__ == '__main__':    
    params(1,2)  
    params(1,2,3,4)  
    params(1,2, op2=4)
    params(1,2, op2=4, op1=0) 
    params(1,2,3,4,5,6,7,8,x=1,y=2,z=3)
    print(type(params), params.__doc__, params.__name__)

    
