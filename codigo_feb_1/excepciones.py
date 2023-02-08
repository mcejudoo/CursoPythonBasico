"""
Capturar errores en Python
"""

def test1():
    # Capturar excepciones específicas:
    try:
        L = list(range(10))
        L.index(1)

        s = "hola"
        print(s[0])

        print(8//0)

    except ValueError as e:
        print('Error: ', e)

    except IndexError as e:
        print('Error: ', e)

    except Exception as e:
        print(e.__class__.__name__,  e)

def test2():
    # Capturar excepciones específicas agrupando en una tupla
    try:
        L = list(range(10))
        L.index(1)

        s = "hola"
        print(s[10])

        print(8//1)

    except (ValueError, IndexError) as e:
        print('ValueError o IndexError: ', e)

    except Exception as e:
        print(e.__class__.__name__,  e)

if __name__ == '__main__':
    test2()