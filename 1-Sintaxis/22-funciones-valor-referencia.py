# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:06:42 2020

@author: Gris
"""
#Referencia -> Listas 
def doblarValores(numeros):
	for i in range(0,len(numeros)-1):
		numeros[i] *= 2

ns=[2,4,8,10,12,14]
print("Lista inicial")
print(ns)
doblarValores(ns)
print("Lista duplicada")
print(ns)

#Valor 
def numero(a):
	a=5
	print("Valor de 'a' dentro de la funcion: %d"%(a))

a=15
print("Valor de 'a' antes de la funcion: %d"%(a))
numero(a)


#Paso por referencia
#Se manda la variable(direccion de memoria) 
#y sus datos ya son modificados en la función
#Siempre para tipos de datos compuestos
#Listas, diccionarios, conjuntos....
c1 =[1,2,3]
def duplicar(c):
	for i,n in enumerate(c):
		c[i]= c[i]*2
		print(c[i])

print("Lista c1")
print(c1)
print("Lista c1 duplicada")
print(duplicar(c1))


#Simular dato simple como referencia
n=10
def duplicar(n):
	n = n*2
	return n

print(n)
n = duplicar(n)
print(n)

#simular dato compuesto pase como valor
duplicar(c2[:]) #llamada a la funcion mandando la copia de la variable

