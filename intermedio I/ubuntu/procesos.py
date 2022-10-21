import os, subprocess

def prueba1():
	pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

	for pid in pids:
		try:
			print (open(os.path.join('/proc', pid, 'cmdline'), 'rb').read())
		except IOError: # proc has already terminated
			continue
			
			
def prueba2():
	print ("lista procesos:")
	for p in os.listdir('/proc'):
		print (p)
	

def prueba3():	
	pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]
	print (pl)


#print "Ejecucion prueba1"
#prueba1()

#print "\nEjecucion prueba2"
#prueba2()

print ("\nEjecucion prueba3")
prueba3()

	
