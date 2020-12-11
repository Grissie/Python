# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:54:41 2020

@author: Gris
"""

x=10
y=20
#Evalua una condicion
if(x>y):
    print("%d es mayor que %d"%(x,y))
    
#Sentencia elif
print()
if(x>y):
    print("%d es mayor que %d"%(x,y))
elif(y>x):
    print("%d es mayor que %d"%(y,x))
    
#Sentencia else
z=50
print()
if(z<x):
    print("%d es mayor que %d"%(x,z))
elif(z<y):
    print("%d es mayor que %d"%(y,z))
else:
    print("%d es mayor que %d y que %d"%(z,x,y))

#Simulando un switch en Python
opcion = 3
print()
if(opcion == 1):
	print("Soy la opcion 1")
elif(opcion == 2):
	print("Soy la opcion 2")
elif(opcion == 3):
	print("Soy la opcion 3")
else:
	print("No soy ninguna opcion")

"""
Programa que nos dice si un numero ingresado por el usuario es entero o real
"""
numero = int(input('Proporciona un número: '))
if numero % 2 == 0 :
	print('es par')
else: 
	print('es impar')
	if numero % 3 == 0 :
		print('es multiplo de 3')
	if numero % 5 == 0 :
		print('es multiplo de 5')
	if numero % 7 == 0 :
		print('es multiplo de 7')
	if  numero % 3 != 0 or numero % 5 != 0 or numero % 7 != 0:
		print('tu nombre')