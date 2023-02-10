"""
Ejemplo de socket para un cliente
"""
import socket

HOST="localhost"  # 127.0.0.1
PUERTO=8888

sock_c = None
try:
    # Crea un socket para el cliente:
    sock_c = socket.socket()

    # Se conecta con el servidor:
    sock_c.connect((HOST, PUERTO))

    while True:
        mensaje = input('Mensaje> ')
        if mensaje == '': continue
        
        # Enviamos un mensaje al server:
        sock_c.send(mensaje.encode('utf-8'))

        if mensaje.lower() == 'fin':
            break

        # Esperar el mensaje del Servidor:
        mensajeSer = sock_c.recv(1024)
        mensajeSer = mensajeSer.decode('utf-8')
        print("El Server dice: ", mensajeSer)

except Exception as e:
    print("ERROR", e)
    
except KeyboardInterrupt as e:
    print("Interrupcion de teclado")
    sock_c.send("fin".encode('utf-8'))

finally:
    if sock_c != None:
        sock_c.close()

