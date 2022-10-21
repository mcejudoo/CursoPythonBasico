"""
Implementación de un servidor TCP
"""

import socket as s
import sys

if len(sys.argv) == 2:
    puerto = int(sys.argv[1])
    print('Puerto: ', puerto)

    s_server = s_client = None
    try:
        # Crear un socket TCP / AF_INET
        s_server = s.socket()
        s_server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        print('Socket creado ...')

        # Bind:
        s_server.bind(("localhost",puerto))
        print("Bind ok!")

        # Comunicacion 1 a 1:
        s_server.listen(1)

        print('Servidor a la espera de clientes')
        s_client, addr = s_server.accept()

        print('cliente conectado: ', addr)
        while True:
            # Recibir:
            mensaje = s_client.recv(1024)
            mensaje = mensaje.decode('utf-8')
            if mensaje.lower() == 'fin':
                break

            print('Mensaje del cliente: ', mensaje)
            s_client.send(mensaje.upper().encode('utf-8'))

        print('Fin de comunión')    

    except Exception as e:
        print("ERROR: ", e)

    except KeyboardInterrupt as e1:
        print('Servidor Control+C')

    finally:
        if s_client: s_client.close()
        if s_server: s_server.close()

else:
    print('No se ha indicado el puerto para conectar ...')