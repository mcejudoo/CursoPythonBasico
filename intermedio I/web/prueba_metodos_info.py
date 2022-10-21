#-*-coding: cp1252 -*-
try:
	import urllib2
except ImportError:
	import urllib.request as urllib2
	import urllib.parse

try:
        urlm = "http://www.python.org"
        params = urllib.parse.urlencode({"login": "***", "password": "***"})
        
        f = urllib2.urlopen(urlm, params)
        print (f.info())
        print (f.geturl())
        #print (f.read())
        f.close()

except Exception as e:
        print ("Ocurrió un error")      
        print (e)
        raise e


        
