mi_diccionario = {'nombre':'juan','curso':'sql', 'nota': 7.2}
mi_diccionario['nueva_clave'] = 2
print(mi_diccionario)
del mi_diccionario['nueva_clave']
print(mi_diccionario)
mi_diccionario['nota']= 8.9
print(mi_diccionario)
# comprobar si existe alguna clave en especial
if 'curso' in mi_diccionario:
    print("existe dicha clave")

edades = { "Juan": 30, "María": 25, "Carlos": 35 }
print(edades)
nombre = "Ana"
edad = edades.get(nombre)

if edad is not None:
    print(nombre, "tiene", edad, "años.")

else:
    print(nombre, "no está en el diccionario de edades.")
print('--- tamaño del diccionario len')
print(len(edades))
#funciones de diccionarios
# keys() devuelve una lista de las claves del diccionario
claves = mi_diccionario.keys()
print(claves)

# values() devuelve una lista de los valores del diccionario

valores = mi_diccionario.values()
print(valores)

# items() recibe una lista de tuplas ( clave, valor)
items= mi_diccionario.items()
print(items)

# get() devuelve el valor asociado a una clave o un valor por defecti si la clave no existe
nombre = mi_diccionario.get('nombre')
edad = mi_diccionario.get('edad', 0)
print(nombre,edad)