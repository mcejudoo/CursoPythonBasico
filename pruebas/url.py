# prueba con urllib2

try:
	# python 3
	from urllib.request import urlopen
	
except ImportError:
	# python 2
	from urllib2 import urlopen
	
try:
	f = urlopen("http://www.python.org")	
	print(f.read())
	print("getUrl:", f.geturl())
	f.close()
	
except HTTPError as e:
	print("ERROR:", e)
	print(e.code)
	
except URLError:
	print("ERROR: ", e)		
	print(e.code)
