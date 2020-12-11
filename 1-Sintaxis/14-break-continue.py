# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:10:47 2020

@author: Gris
"""

#Sentencia break para romper ciclos, como: for o while
#En rango va del 1 al 49 
for i in range(1, 50):
	if(i == 20):
		break
	print(i)
print("Sali del bucle")
print()


#Sentencia continue
#Termina la iteracion actual y continua con la siguiente
for i in "Python":
	if(i == "h"):
		continue
	print(i)
print()


x = 2
while(x < 20):
	if(x == 10):
		break
	print(x)
	x += 1 # x = x + 1
    
for x in range(1,21):
    if(x == 10):
        continue
    print(x)

for x in "Hola mundo":
	if(x == "m"):
		continue
	print(x)

