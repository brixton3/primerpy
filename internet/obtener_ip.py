import socket

# Obtener el nombre del host
nombre_host = socket.gethostname()

# Obtener la dirección IP
direccion_ip = socket.gethostbyname(nombre_host)

print(f"La dirección IP de {nombre_host} es {direccion_ip}")