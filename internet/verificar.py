import socket

try:
    socket.gethostbyname('google.com')
    c = socket.create_connection(('google.com', 80), 1)
    c.close()
    print("Conexión exitosa a google.com")
except socket.gaierror as e:
    print("Error de DNS:", e)
except socket.error as e:
    print("Error de conexión:", e)