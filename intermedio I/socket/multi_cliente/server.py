# Servidor receptor de ficheros:
from socket import *
from threading import Thread

class HiloServer(Thread):
	
	def __init__(self, cliente, addr):
		Thread.__init__(self)
		self.__cliente = cliente
		self.__addr = addr
		
	def run(self):	
		try:	
			while True:		
				# Esperar datos del cliente:
				data = self.__cliente.recv(1024) 
				data = data.decode('utf-8')
				print(data)

				#Enviar el mensaje al cliente:
				linea = data.upper().encode('utf-8')
				self.__cliente.send(linea) 
				
		except Exception as ex:
			if ex.errno == 10054:
				print("Cliente Desconectado")
			else:
				print(ex)
			#input()
	

class Server(object):
	
	def __init__(self, host, puerto, num_conexiones):
		self.__host = host
		self.__puerto = puerto
		self.__num_conexiones = num_conexiones
		
		
	def iniciar(self):
		try:
			sock = socket()
			sock.bind((self.__host, self.__puerto))
			sock.listen(self.__num_conexiones)
			
			print("Servidor ON en puerto:", self.__puerto)
			
			while True:
				# Aceptar conexiones de los clientes:
				print("Esperando clientes")
				cliente, addr = sock.accept()
				print("Cliente conectado ",addr)
				
				hilo = HiloServer(cliente, addr)
				hilo.start()
				
		except Exception as ex:
			print(ex)
			input()
			
			
						
		
if __name__=='__main__':
	server = Server("localhost", 5001, 5)
	server.iniciar()
	
