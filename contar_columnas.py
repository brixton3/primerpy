dato= '4312","26794162","1878","La Plata","LP:26794162","op391dma","OPERADOR TELEFÓNICO LA PLATA","op391dma","OPERADOR TELEFÓNICO LA PLATA","op391dma","OPERADOR TELEFÓNICO LA PLATA","","","","0","","","","","","","","","","0.0","0.0","","","","","","SUPERVISOR 911 LA PLATA","","  (Nº 0) e/  y ","2021-10-31 02:55:00.483","2021-10-31 02:55:00.483","2021-10-31 02:56:43.060","No","No","No","","","","","","","","","C","CERRADO","ASOCIADO","","Suceso [LP:26794162] asociado al suceso [LP:26785243]","0","0","0","0","0","0","0","PARTICULAR","","","","1159156224","","","26785243","0","","No","ASOCIADO","Suceso [LP:26794162] asociado al suceso [LP:26785243]","2021-10-31 02:56:43.060","2021-10-31 02:56:43.060","006b032440ace29c","","","","","","","","","","","","'

# Registro de ejemplo
registro = '4311","26794161","957","La Plata","LP:26794161","op297san","OPERADOR TELEFÓNICO LA PLATA","desplopezg","DESPACHADOR ALMIRANTE BROWN","desplopezg","DESPACHADOR ALMIRANTE BROWN","DONATO ALVAREZ","","justo en la qesuina , van hacia el lado de solano. ","557","San Ramon","","","","","AB_27","3","","","-34.754888442673","-58.336446713321003","ALMIRANTE BROWN","ALMIRANTE BROWN","SAN JOSE","","SAN JOSE","CD ALMIRANTE BROWN",""," DONATO ALVAREZ (Nº 557) e/ San Ramon y ","2021-10-31 02:54:56.873","2021-10-31 02:57:16.450","2021-10-31 02:57:36.657","No","No","No","CONTRAVENTORES","DESORDEN EN VÍA PÚBLICA","CONTRAVENTORES (DESORDEN EN VÍA PÚBLICA)","BAJA","CONTRAVENTORES","DESORDEN EN VÍA PÚBLICA","BAJA","CONTRAVENTORES (DESORDEN EN VÍA PÚBLICA)","C","CERRADO","ASOCIADO","","Suceso [LP:26794161] asociado al suceso [LP:26794009]","0","0","0","0","0","0","0","PARTICULAR","","francisco","","1136258375","Llamante refiere que estan pasando 20 personas realizan desorden, no hay armados ni heridos. ","","26794009","0","","No","","","","2021-10-31 02:57:36.657","006b032440ace29e","","","","","","","","","","","","'

# Limpiar el registro (quitar comillas al inicio y al final)
registro_limpio = registro.strip('"')
registro_limpio_dato = dato.strip('"')

# Contar las columnas
columnas = registro_limpio.split('","')  # Separar por comas
columnas_dato = registro_limpio_dato.split('","')  # Separar por comas

# Contar el número de columnas
numero_columnas = len(columnas_dato)
numero_columnas2 = len(columnas)

# Mostrar el resultado
print(f'Número de columnas: {numero_columnas}')
print(f'Número de columnas: {numero_columnas2}')
# print (columnas),
cont=0
# print(columnas[0])
while cont < len(columnas_dato):
    print(cont,">>", columnas_dato[cont], "||", columnas[cont])
    cont=cont+1