
#-*- coding: cp1252 -*-
try:
	import urllib2
except:
	import urllib.request as urllib2	
	
import re

try:
		urlm = "http://transparencia.gob.es/es_ES/buscar/contenido/cibi/CIBI_DPTO26"

		f = urllib2.urlopen(urlm)
		html = f.read()
		f.close()
		
		html=html.decode('utf-8')
		print(html[3000:4000])
        
		for match in re.finditer('<tr>(.*?)</tr>', html,re.DOTALL):
			linea = match.group(0) # prueba match.group(0)
			L = []
			print(linea)

			for match2 in re.finditer('<td.*?>(.*?)</td>', linea,re.DOTALL):
					s = match2.group(1)
					
					pos = s.find('<')
					if pos >= 0:
							for match3 in re.finditer('<span.*?>(.*?)</span>', s,re.DOTALL):
									s = s[:pos]+match3.group(1)
								   
					L.append(s)
			print (L)
			print ("-----")
                

except Exception as e:
        print ("Ocurrió un error", e)


        
