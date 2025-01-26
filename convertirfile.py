import os
import shutil
from datetime import datetime, timedelta

def convertir_archivo(ruta_archivo, carpeta_destino):
    nombre_archivo = os.path.basename(ruta_archivo)
    fecha_str = nombre_archivo[:8]
    categoria = nombre_archivo[8:].split('.')[0]  # Obtener la categoría sin la extensión
    
    # Convertir la fecha al formato dd-mm-aaaa y restar un día
    fecha = datetime.strptime(fecha_str, '%Y%m%d')
    fecha -= timedelta(days=1)
    fecha_formateada = fecha.strftime('%d-%m-%Y')
    
    # Crear el nuevo nombre del archivo
    nuevo_nombre = f"{fecha_formateada}.csv"
    
    # Crear la ruta completa del archivo de destino
    ruta_destino = os.path.join(carpeta_destino, categoria, nuevo_nombre)
    
    # Crear la carpeta de destino si no existe
    os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
    
    # Copiar el archivo a la nueva ubicación con el nuevo nombre
    shutil.copy(ruta_archivo, ruta_destino)
    print(f"Archivo copiado a: {ruta_destino}")

# Ejemplo de uso de 2025
ruta_archivo = 'd:/datos/20241221LP.csv'
carpeta_destino = 'd:/datos/destino'
convertir_archivo(ruta_archivo, carpeta_destino)