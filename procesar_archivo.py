import pandas as pd

# Ruta del archivo de texto que contiene los nombres de los archivos
ruta_archivo_txt = 'lista_archivos.txt'

# Lista para almacenar las fechas
fechas = []

# Leer los nombres de los archivos del archivo de texto
with open(ruta_archivo_txt, 'r') as file:
    for linea in file:
        nombre_archivo = linea.strip()  # Quitar espacios en blanco y saltos de línea
        try:
            # Convertir el nombre del archivo a fecha
            fecha = pd.to_datetime(nombre_archivo.split('.')[0], format='%d-%m-%Y')  # Cambia el formato según sea necesario
            fechas.append(fecha)
        except ValueError:
            print(f"El archivo {nombre_archivo} no contiene una fecha válida.")

# Ordenar las fechas
fechas_ordenadas = sorted(fechas)

# Mostrar las fechas ordenadas
for fecha in fechas_ordenadas:
    print(fecha.strftime('%d-%m-%Y'))