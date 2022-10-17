#-*- coding:cp1252 -*-

import threading, time

class MiThread(threading.Thread): 
	def __init__(self, evento): 
		threading.Thread.__init__(self) 
		self.evento = evento 

	def run(self): 
		print (self.getName(), "esperando al evento" )
		self.evento.wait() 
		print (self.getName(), "termina la espera")

evento = threading.Event()
t1 = MiThread(evento)
t1.start()
t2 = MiThread(evento)
t2.start()
# Esperamos un poco
time.sleep(2)
evento.set()
