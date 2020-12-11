# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:06:46 2020

@author: Gris
"""

#Entrada de datos 
entero=int(input("Ingresa un entero: "))
flotante=float(input("Ingrese un flotante: "))
valores=[]
for i in range(1,11):
    valores.append(input("Ingrese un valor en [%d]: "%(i-1)))
    
#Imprimiendo los datos
print("Numero entero: %d"%entero)
print("Numero decimal: %d"%flotante)
print("Imprimiendo la lista")
for i in valores:
    print(i)

#Salida de los datos 
cad="texto"
num=10
print("\nEste es un",cad," y este un numero ",num)
print("Esto es '{0}' y un numero '{1}'".format(cad,num))
print("Esto es '{texto}' y un numero '{numero}'".format(texto=cad,numero=num))

#20 caracteres a la derecha, como espacio
print("{:>20}".format("Palabra")) 
#20 caracteres a la izquierda 
print("{:20}".format("Palabra"))
#30 caracteres al centro
print("{:^20}".format("Palabra"))  
#Truncamiento a dos caracteres
print("{:.2}".format("Palabra"))  

print()
#Formateo de numeros enteros rellenados con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
#Formateo de numeros enteros rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print()
#Formateo de numeros flotantes, rellenados con espacios
print("{:7.3f}".format(3.1415161814)) #7 Espacios y 3 decimales
print("{:07.3f}".format(3.1415161814)) #7 Espacios con ceros y 3 decimales