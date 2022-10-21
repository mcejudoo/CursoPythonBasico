# pruebas con las cadenas:

s = "hola que tal estas hoy lunes"

n = s.count("a")
print ("n: ", n)

pos = s.find("la")
if pos == -1:
        print ("la no existe en la cadena")
else:
        print ("existe en la cadena en: ", pos)


pos = s.rfind('a')
if pos == -1:
        print ("na no existe en la cadena")
else:
        print ("existe en la cadena en: ", pos)



try:
        pos2 = s.index("las")
        print ("las existe en la pos: ", pos2)
        
except Exception as e:
        print ("Error: ", e)

        
t=s.partition("a")
print (t)

ss=s.replace("a","xxx")
print (ss)

L=s.split("a")
print (L)

s2 = s.capitalize()
print (s2)

        
