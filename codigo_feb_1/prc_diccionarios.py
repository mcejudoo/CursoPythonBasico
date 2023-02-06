"""
Calcular un histograma a nivel de letra y/o palabra
"""
texto = """Habitualmente se entiende por palíndromo aquel que toma por unidad 
la letra, es decir, cuya última letra es la misma que la primera, la penúltima 
es la misma que la segunda, etc. Es el caso de palabras tales como reconocer o anilina. 
Sin embargo, también se puede tomar como unidad la sílaba (por ejemplo, gato con toga, 
aunque en este caso podría ser calificado como anagrama), 
la palabra o incluso el renglón."""

# Recuento por letra:
d1 = {}
for i in texto:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)

# Solución 2:
d2 = dict()
letras = set(texto)
for i in letras:
    d2[i] = texto.count(i)
print(d2)

# Lo mismo por palabras:
palabras=texto.replace('\n','').split(' ')
k3=dict()
for i in palabras:
    k3[i]=texto.count(i)
print(k3)

