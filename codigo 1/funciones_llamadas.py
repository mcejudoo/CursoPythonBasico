"""
Ejemplos de llamadas en python
"""

def segundos(h,m,s):
    """
    Convierte h,m,s a segundos
    """
    return h*3600 + m*60 + s

if __name__ == "__main__":
    # Forma posicional
    print(segundos(12,30,15))  

    # Forma nominal
    print(segundos(s=15, h=12, m=30))

    # Con una tupla
    t = (12,30,15)
    print(segundos(t[0],t[1],t[2]))

    print(segundos(*t)) # Expande la tupla a los 3 parametros

    # Con un dict
    d = {"h":12,"m":30,"s":15}
    print(segundos(**d))

    # Con una lista
    L = [12,30,45]
    print(segundos(*L))

    # Definir una lista de horas aleatorias (con tripletas: tuplas) y luego
    # convertirlas en segundos y almacenar el resultado en otra lista


    


