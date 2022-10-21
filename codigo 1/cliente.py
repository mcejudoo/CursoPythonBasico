"""
Implementación del cliente TCP
"""

import socket as s
import sys

if len(sys.argv) == 2:
    puerto = int(sys.argv[1])
    print('Puerto: ', puerto)

    s_client = None
    try:
        # Crear el socket
        s_client = s.socket()

        # Conectar: 
        s_client.connect(("localhost",puerto))
        print('Cliente conectado ...')

        while True:
            mensaje = input("Introduce un mensaje: ")
            s_client.send(mensaje.encode('utf-8'))

            if mensaje.lower() == 'fin':
                break

            recibido = s_client.recv(1024)
            recibido = recibido.decode('utf-8')
            print('Mensaje del servidor: ', recibido)

    except Exception as e:
        print("ERROR: ", e)

    except KeyboardInterrupt as e1:
        print('Servidor Control+C')

    finally:
        if s_client: s_client.close()

else:
    print('No se ha indicado el puerto para conectar ...')        

