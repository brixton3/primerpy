#dato= '4312","26794162","1878","La Plata","LP:26794162","op391dma","OPERADOR TELEFÓNICO LA PLATA","op391dma","OPERADOR TELEFÓNICO LA PLATA","op391dma","OPERADOR TELEFÓNICO LA PLATA","","","","0","","","","","","","","","","0.0","0.0","","","","","","SUPERVISOR 911 LA PLATA","","  (Nº 0) e/  y ","2021-10-31 02:55:00.483","2021-10-31 02:55:00.483","2021-10-31 02:56:43.060","No","No","No","","","","","","","","","C","CERRADO","ASOCIADO","","Suceso [LP:26794162] asociado al suceso [LP:26785243]","0","0","0","0","0","0","0","PARTICULAR","","","","1159156224","","","26785243","0","","No","ASOCIADO","Suceso [LP:26794162] asociado al suceso [LP:26785243]","2021-10-31 02:56:43.060","2021-10-31 02:56:43.060","006b032440ace29c","","","","","","","","","","","","'
dato ='2339","26628154","1926","La Plata","LP:26628154","op291vyd","OPERADOR TELEFÓNICO LA PLATA","desprodriguezch","JEFE SERVICIOS ISLAS","desprodriguezch","JEFE SERVICIOS ISLAS","PARANA MINI","","MUELLE DON JOSE ","0","CHANA ","","","","","","","","","0.0","0.0","","ISLAS","","","ISLAS","CD ISLAS",""," PARANA MINI (Nº 0) e/ CHANA  y ","2021-10-21 04:04:23.853","2021-10-21 04:06:04.047","2021-10-21 04:13:11.920","No","No","No","EMERGENCIA DE SALUD","EMERGENCIA","EMERGENCIA DE SALUD (EMERGENCIA)","ALTA","EMERGENCIA DE SALUD","EMERGENCIA","ALTA","EMERGENCIA DE SALUD (EMERGENCIA)","C","CERRADO","DERIVADO A 107","","","0","0","0","0","0","0","0","PARTICULAR","","EZEQUIEL ","","1164139459","LLAMANTE REFIERE QUE  LA NOVIA DE 20 AÑOS  FUE ATACADA POR 7 PERROS ESTA MUY HERIDA","","-1","0","","No","","","","2021-10-21 04:13:11.920","006b032440a937b8","","","","","","","","","","","","'
# Registro de ejemplo para pruebas
#registro = '4311","26794161","957","La Plata","LP:26794161","op297san","OPERADOR TELEFÓNICO LA PLATA","desplopezg","DESPACHADOR ALMIRANTE BROWN","desplopezg","DESPACHADOR ALMIRANTE BROWN","DONATO ALVAREZ","","justo en la qesuina , van hacia el lado de solano. ","557","San Ramon","","","","","AB_27","3","","","-34.754888442673","-58.336446713321003","ALMIRANTE BROWN","ALMIRANTE BROWN","SAN JOSE","","SAN JOSE","CD ALMIRANTE BROWN",""," DONATO ALVAREZ (Nº 557) e/ San Ramon y ","2021-10-31 02:54:56.873","2021-10-31 02:57:16.450","2021-10-31 02:57:36.657","No","No","No","CONTRAVENTORES","DESORDEN EN VÍA PÚBLICA","CONTRAVENTORES (DESORDEN EN VÍA PÚBLICA)","BAJA","CONTRAVENTORES","DESORDEN EN VÍA PÚBLICA","BAJA","CONTRAVENTORES (DESORDEN EN VÍA PÚBLICA)","C","CERRADO","ASOCIADO","","Suceso [LP:26794161] asociado al suceso [LP:26794009]","0","0","0","0","0","0","0","PARTICULAR","","francisco","","1136258375","Llamante refiere que estan pasando 20 personas realizan desorden, no hay armados ni heridos. ","","26794009","0","","No","","","","2021-10-31 02:57:36.657","006b032440ace29e","","","","","","","","","","","","'
registro='2340","26628155","958","La Plata","LP:26628155","op307rln","OPERADOR TELEFÓNICO LA PLATA","despsilvestre","DESPACHADOR SAN MIGUEL","despsilvestre","DESPACHADOR SAN MIGUEL","LETONIA","","ESQUINA ","0","Mstro Eduardo Ferreyra","","","","","SL_15","3","","","-34.5575942993","-58.757747650100001","SAN MIGUEL","SAN MIGUEL","SAN MIGUEL","","SAN MIGUEL","CD SAN MIGUEL",""," LETONIA (Nº 0) e/ Mstro Eduardo Ferreyra y ","2021-10-21 04:04:35.897","2021-10-21 04:05:58.547","2021-10-21 04:12:19.730","No","No","No","ROBO","VÍA PÚBLICA","ROBO (VÍA PÚBLICA)","ALTA","ROBO","VÍA PÚBLICA","ALTA","ROBO (VÍA PÚBLICA)","C","CERRADO","NEGATIVO","","","0","0","0","0","0","0","0","PARTICULAR","MONICA ","","","1128205427","REF QUE  ESTAN ROBANDO LOS CABLES  4 ARRIBA DE LOS PALOS Y UNO EN LA ESQUINA, NO VE SI ESTAN ARMADOS, ESTAN A PIE ____EN PROCESO ","","-1","0","","No","","","","2021-10-21 04:12:19.730","006b032440a937b9","","22095	oa roman ofl franco","PATRULLERO","22095	oa roman ofl franco","2021-10-21 04:07:00.860","2021-10-21 04:06:11.713","2021-10-21 04:12:00.097","2021-10-21 04:12:19.510","0h 7m 25s ","0h 5m 49s ","0h 5m 0s ","0h 7m 44s '
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