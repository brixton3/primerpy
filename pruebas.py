# multiples variables en python
x= y= z = 10
print(x, y, z )

xx, yy, zz = "banana","pera","manzana"
print (xx)

fruits = ['apple','banana','cherry']
a, b, c= fruits
print(a)

# output variables

print('Hello', 'World')

a = 'Hello'
b = 'World'
print(a + b)

a = 4
b = 5
print(a + b)

# global variables

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)

# usando la palabra global antes del nombre de la variable
global yglobalita
yglobalita= 23
print (yglobalita)

# Data types
#type list
x = ["apple", "banana", "cherry"]
print(type(x))
#type tuple
x = ("apple", "banana", "cherry")
print(type(x))
#type dict
x = {"name" : "John", "age" : 36}
print(type(x))

x = True
print(type(x))

x = 5
x = complex(x)
print(type(x))