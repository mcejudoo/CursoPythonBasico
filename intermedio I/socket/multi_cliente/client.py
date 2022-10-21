# Cliente socket
from socket import *

class Client(object):
	
	def __init__(self, host, puerto):
		self.__host = host
		self.__puerto = puerto
		
	
	def iniciar(self):
		try:
			# Crear el socket
			sock = socket()
			
			# Conectar con el server:
			sock.connect((self.__host, self.__puerto))
			
			while True:
				print ("Texto para enviar al Server")
				cadena = input()
				
				sock.send(cadena.encode('utf-8'))
				
				respuesta = sock.recv(1024)
				print(respuesta)
			
		except Exception as ex:
			print (ex)
			input()
			
	
	
if  __name__=='__main__':
	cliente = Client("localhost", 5001)
	cliente.iniciar()
