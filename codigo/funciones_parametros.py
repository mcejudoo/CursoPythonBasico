"""
Tipos de parámetros en una función de Python
"""

def params(ob1,ob2,op1=10,op2=20):
    print("obligatorios: ", ob1, ob2)
    print("opcionales: ", op1, op2)
    print()


if __name__ == '__main__':
    params(1,2)  
    params(1,2,3,4)  
    params(1,2, op2=4)
    params(1,2, op2=4, op1=0)

    
