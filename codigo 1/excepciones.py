"""
Control de excepciones en python
"""

class ColeccionError(Exception):

    def __init__(self,mensaje=""):
        Exception.__init__(self,mensaje)        

    def __str__(self):
        return "ERROR: " + Exception.__str__(self)

def funcion1(index):
    try:
        L = list(range(10))
        d = {15:"A",16:"B",17:"C",18:"D",19:"E"}
        print(d[index])
        print(L[index])

    except (IndexError,KeyError) as e:
        print("Error:",e)
        raise ColeccionError('El parametro index no es correcto')

    except Exception as e:
        raise e

def testFuncion1(index):
    try:
        funcion1(index)
    except Exception as e:
        print(e.__class__.__name__,e)

if __name__ == '__main__':
    testFuncion1(0)    
