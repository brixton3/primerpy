# probar
import os
import pandas as pd

# Ruta de la carpeta donde están los archivos Excel
carpeta = 'ruta/a/tu/carpeta'

# Lista para almacenar las fechas
fechas = []

# Iterar sobre los archivos en la carpeta
for archivo in os.listdir(carpeta):
    # Comprobar si el archivo es un archivo Excel
    if archivo.endswith('.xlsx') or archivo.endswith('.xls'):
        # Extraer la fecha del nombre del archivo (suponiendo que el formato es 'YYYY-MM-DD.xlsx')
        fecha_str = archivo.split('.')[0]  # Quita la extensión
        try:
            fecha = pd.to_datetime(fecha_str, format='%Y-%m-%d')  # Cambia el formato según sea necesario
            fechas.append(fecha)
        except ValueError:
            print(f"El archivo {archivo} no contiene una fecha válida.")

# Ordenar las fechas
fechas_ordenadas = sorted(fechas)

# Mostrar las fechas ordenadas
for fecha in fechas_ordenadas:
    print(fecha.strftime('%Y-%m-%d'))