# busca horas dentro de una cadena:

import re

s = "4:05:56 31/05/1987 4:05:56 contenido de log 07:09:23 mas contenidos ..."

# match falla porque la cadena tiene que empezar por el patron
r1 = re.match(r"contenido", s)
r2 = re.match(r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9]", s)
r3 = re.match(r"[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", s)

print ("\nmatch")
print (r1,r2)

if r3 != None:
        print (dir(r3))
        print (r3.start())
        print (r3.end())
        print (r3.group())
        print (r3.groups())
        print (r3.string)


# search en cualquier posicion de la cadena:
r1 = re.search("Contenido", s)
r2 = re.search(r"([0-9][0-9]:[0-9][0-9]:[0-9][0-9])", s)
r3 = re.search(r"([0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2})", s)
r4 = re.search(r"(\d{1,2}:\d{1,2}:\d{1,2})", s)

print ("\nsearch")
if r1 != None:
        print ("search1 ", r1.groups())

if r2 != None:
        print ("search2 ",r2.groups())

if r3 != None:
        print ("search3 ",r3.groups())

if r4 != None:
        print ("search4 ",r4.groups())

# Para extraer todas las horas lo hacemos con findall:
# Con r delante indica cadena tipo raw, no interpreta los chars especiales
r1 = re.findall(r"contenido", s)
r2 = re.findall(r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9]", s)
r3 = re.findall(r"[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", s)
r4 = re.findall(r"\d{1,2}:\d{1,2}:\d{1,2}", s)

print ("\nfindall")
print (r1)
print (r2)
print (r3)
print (r4)

print ("\ngroup y finditer")
# Ejemplo de finditer: para extraer contenidos:
line = 'bla bla bla<form>Form 1</form> some text...<form>Form 2</form> more text?'
for match in re.finditer('<form>(.*?)</form>', line):
    print (match.group(1)) # prueba match.group(0)



        
